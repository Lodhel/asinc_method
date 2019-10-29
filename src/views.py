import datetime
import json

from aiohttp import web
from aiohttp_session import get_session

import pymongo

routes = web.RouteTableDef()


@routes.view("/")
class MainViewSet(web.View):

    def db_operation(self, session):
        conn = pymongo.MongoClient('localhost', 27017)
        db = conn['mongodb']
        coll = db['sessions']

        coll.save({"time": datetime.datetime.now(), "session": session})

    async def get(self):
        session = get_session(self.request)
        cookie = await session.cr_frame.f_locals["request"].cookies
        data = {'session': str(cookie)}
        self.db_operation(cookie)
        yield web.json_response(data)

    async def post(self):
        data = {'request': 'info'}
        await web.json_response(data)


@routes.view("/chat/")
class WebSocketViewSet(web.View):

    def create_message(self, data):
        message = json.dumps(data)
        return message

    async def get(self):
        ws = web.WebSocketResponse()
        ws.prepare(self.request)
        ws_array = []

        # session = MainViewSet().get()
        ws_array.append(ws)

        for client in ws_array:
            #message = self.create_message({"data": "data"})
            client.send_str(data="Hello World")

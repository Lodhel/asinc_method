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

        coll.save({"time": "NaN", "session": session})

    async def get(self):
        session = get_session(self.request)
        cookie = session.cr_frame.f_locals["request"].cookies
        data = {'session': str(cookie)}
        self.db_operation(cookie)
        return web.json_response(data)

    async def post(self):
        data = {'request': 'info'}
        await web.json_response(data)

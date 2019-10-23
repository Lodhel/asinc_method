from aiohttp import web
from aiohttp_session import get_session


routes = web.RouteTableDef()


@routes.view("/")
class MainViewSet(web.View):
    async def get(self):
        session = get_session(self.request)
        cookie = session.cr_frame.f_locals["request"].cookies
        data = {'session': str(cookie)}
        return web.json_response(data)

    async def post(self):
        data = {'request': 'info'}
        await web.json_response(data)

from aiohttp import web
from aiohttp_session import get_session


routes = web.RouteTableDef()


@routes.view("/")
class MainViewSet(web.View):
    async def get(self):
        data = {'request': 'info'}
        return web.json_response(data)

    async def post(self):
        data = {'request': 'info'}
        return web.json_response(data)

"""
@routes.view("api/user/")
class UserViewSet(web.View):

    async def handler(self, request):
        session = await get_session(request)
        last_visit = session['last_visit'] if 'last_visit' in session else None
        text = 'Last visited: {}'.format(last_visit)
        return web.Response(text=text)
"""
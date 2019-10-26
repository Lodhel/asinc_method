from aiohttp import web

import base64
from cryptography import fernet
from aiohttp_session import setup
from aiohttp_session.cookie_storage import EncryptedCookieStorage
from views import routes


from motor import motor_asyncio as ma


app = web.Application()
fernet_key = fernet.Fernet.generate_key()
secret_key = base64.urlsafe_b64decode(fernet_key)
setup(app, EncryptedCookieStorage(secret_key))
app.router.add_routes(routes)


app.client = ma.AsyncIOMotorClient("127.0.0.1")
app.db = app.client["mongodb"]


web.run_app(app)
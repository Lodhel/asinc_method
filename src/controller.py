from aiohttp import web

import base64
from cryptography import fernet
from aiohttp_session import setup
from aiohttp_session.cookie_storage import EncryptedCookieStorage
from views import routes


app = web.Application()
fernet_key = fernet.Fernet.generate_key()
secret_key = base64.urlsafe_b64decode(fernet_key)
setup(app, EncryptedCookieStorage(secret_key))
app.router.add_routes(routes)

web.run_app(app)
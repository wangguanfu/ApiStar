from apistar.backends import sqlalchemy_backend
from apistar.frameworks.wsgi import WSGIApp as App
from apistar import commands

from app.routes import routes
from core.config import settings

app = App(routes=routes,
          settings=settings,
          commands=sqlalchemy_backend.commands,
          components=sqlalchemy_backend.components
          )

if __name__ == '__main__':
    app.main()

    # how to publish culinary
    # add admin account manual in Database
    # login admin in 127.0.0.1/docs ( autentication - basic ) and add publisher
    # login publisher and add your culinary


from apistar import Include, Route
from apistar.handlers import docs_urls, static_urls

from .views import add_admin
from .views import add_publisher, put_publisher, delete_publisher, get_publisher
from .views import add_culinary, get_culinary
from .views import get_token

admin = [
    Route('add_admin', 'POST', add_admin)
]
token = [
    Route('get_token', 'POST', get_token)
]
publisher = [
    Route('get_publisher', 'POST', get_publisher),
    Route('add_publisher', 'POST', add_publisher),
    Route('put_publisher', 'PUT', put_publisher),
    Route('delete_publisher', 'DELETE', delete_publisher)
]
culinary = [
    Route('get_culinary', 'GET', get_culinary),
    Route('add_culinary', 'POST', add_culinary),
]

routes = [
    Include('/', admin),
    Include('/', token),
    Include('/', publisher),
    Include('/', culinary),
    Include('/docs', docs_urls),
    Include('/static', static_urls)
]

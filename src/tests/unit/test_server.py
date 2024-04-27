from app import server
from blacksheep import Application


def test_app_is_created():
    app = server.create_app()
    assert isinstance(app, Application)

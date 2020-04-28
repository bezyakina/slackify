import pytest
from src.flask_slack.flack import Flack


@pytest.fixture
def client(test_app):
    test_app.config['TESTING'] = True

    with test_app.test_client() as client:
        yield client


@pytest.fixture
def bare_client():
    app = Flack('testing')
    app.config['TESTING'] = True

    @app.default
    def unknown_command():  # TODO: Review this
        return 'Unknown Command'

    with app.test_client() as client:
        yield client


@pytest.fixture(scope="session")
def test_app():
    app = Flack('testing')

    @app.command(name='chau')
    def hello():
        return 'Hello'

    @app.shortcut('my-shortcut')
    def shortcut():
        return 'Shortcut'

    @app.action(id='my-action-id')
    def my_action():
        return 'Action'

    @app.action(action_id='the-id', block_id='a-block-id')
    def complex_action():
        return 'Complex Action'

    @app.view('my-first-view')
    def my_view():
        return 'View'

    @app.default
    def unknown_command():
        return 'Unknown Command'

    return app

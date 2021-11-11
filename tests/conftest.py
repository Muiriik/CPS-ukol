import pytest
from CPS_xml_to_json import create_app

@pytest.fixture
def app():
  app = create_app({
    'TESTING': True,
  })

  yield app

@pytest.fixture
def client(app):
  """A test client for the app."""
  return app.test_client()

@pytest.fixture
def runner(app):
  """A test runner for the app's Click commands."""
  return app.test_cli_runner()
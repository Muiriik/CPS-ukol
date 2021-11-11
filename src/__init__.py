from flask import Flask

def create_app(test_config=None):

  """Create and configure an instance of the Flask application."""
  app = Flask(__name__)
  app.config.from_mapping(
    # a default secret that should be overridden by instance config
    SECRET_KEY="dev",
  )

  if test_config is None:
    # load the instance config, if it exists, when not testing
    app.config.from_pyfile("config.py", silent=True)
  else:
    # load the test config if passed in
    app.config.update(test_config)


  from src.main import convert_blueprint
  app.register_blueprint(convert_blueprint)

  return app


from flask import Flask
app = Flask(__name__, instance_relative_config=True)

from . import blog
app.register_blueprint(blog.bp)
app.add_url_rule('/', endpoint='index')
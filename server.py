import gevent
from gevent import monkey

# This is where it should be called
# monkey.patch_all()

from flask import Flask, request, render_template
import bugsnag
from bugsnag.flask import handle_exceptions

# If called here `requests` has already been loaded and will recursively fail
monkey.patch_all()

app = Flask(__name__)

bugsnag.configure(
    api_key = 'YOUR_API_KEY',
)
handle_exceptions(app)

@app.route('/')
def crashdict():
    """Deliberately triggers an unhandled KeyError to be reported by the bugsnag exception handler, and crash the app.
    """
    customheader = request.headers['my-custom-header']
    return 'Received your header: ' + customheader

if __name__ == '__main__':
    app.run(port=3000)

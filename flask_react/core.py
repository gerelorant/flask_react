from flask import Flask, Blueprint, render_template, url_for
import os
try:
    import flask_socketio as sio
    SOCKET_IO = True
except ImportError:
    sio = None
    SOCKET_IO = False


import flask_react.babel as babel


class React:
    """React extension for Flask applications.

    Registers a React blueprint and makes base template available.


    :param index_template (str): Template for index page.
    :param extensions (iter): List of react extensions.
    :param jsx_folder (str): Path to jsx source files.
    :param socket_io (SocketIO): Flask-SocketIO extension instance.

    """
    def __init__(
            self,
            app: Flask = None,
            index_template: str = "react/index.html",
            extensions: iter = None,
            jsx_folder: str = None,
            socket_io = None
    ):
        self.app = None
        self.blueprint = None
        self.index_template = index_template

        if isinstance(extensions, str):
            self.extensions = (extensions, )
        else:
            self.extensions = extensions or ()

        self._jsx_folder = jsx_folder

        self.socket = socket_io

        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask):
        """Initialize extension with Flask instance.

        :param app: Flask instance.
        """
        self.app = app
        self.app.extensions["react"] = self

        self.blueprint = Blueprint(
            name="react",
            import_name=__name__,
            static_folder="static",
            static_url_path='/static/react',
            template_folder="templates",
            url_prefix="/react"
        )
        self.app.config.setdefault("REACT_INDEX_TEMPLATE", self.index_template)
        self.app.config.setdefault("REACT_EXTENSIONS", self.extensions)

        @app.route("/")
        def react_app():
            template = app.config.get("REACT_INDEX_TEMPLATE")
            return render_template(
                template,
                app_url=self.get_url("react/js/App.js"),
                favicon=self.get_url("react/favicon.ico"),
                logo192=self.get_url("react/logo192.png"),
                logo512=self.get_url("react/logo512.png"),
                manifest=self.get_url("react/manifest.json")
            )

        self.app.register_blueprint(self.blueprint)

        self.init_babel()
        self.init_socket()

    def get_url(self, filename: str):
        """Returns URL for file.

        If file does not exist in `static` folder, file from `react.static` is
        returned.

        :param filename: Filename to check.
        :return: URL to file.
        """
        path = os.path.join(self.app.root_path, "static", *filename.split('/'))
        if os.path.exists(path):
            return url_for("static", filename=filename)
        else:
            return url_for("react.static", filename=filename)

    def init_babel(self):
        """Initialize Babel for JSX conversion."""
        if self._jsx_folder:
            babel_path = os.path.join("node_modules", ".bin", "babel")
            if not os.path.exists(babel_path):
                babel.install()

            babel.convert(self._jsx_folder, 'static/react/js/')

    def init_socket(self):
        """Initialize SocketIO extension."""
        if "socket.io" in self.extensions:
            if not SOCKET_IO:
                raise ValueError("Flask-SocketIO is not installed "
                                 "for 'socket.io' extension.")
            if self.socket is None:
                self.socket = sio.SocketIO(self.app)

    def run(self, *args, **kwargs):
        """Shortcut for Flask-SocketIO's run method."""
        if self.socket is not None:
            self.socket.run(*args, **kwargs, log_output=True)
        else:
            self.app.run(*args, **kwargs)

from dash import Dash
from appshell.appshell import create_appshell
from controller.controller import Controller

app = Dash(
    __name__,
    suppress_callback_exceptions=True,
    use_pages=True,
    update_title=None,
)

controller = Controller()
controller.configure()


app.layout = create_appshell()
server = app.server

if __name__ == "__main__":
    app.run_server(debug=True)
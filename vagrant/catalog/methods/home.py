from . import routes


@routes.route('/')
def home():
    return "home"

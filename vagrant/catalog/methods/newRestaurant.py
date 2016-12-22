from . import routes


@routes.route('/restaurant/new')
def newRestaurant():
    return "new restaurant"

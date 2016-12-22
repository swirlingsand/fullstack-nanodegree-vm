from flask import render_template, jsonify, url_for, flash
from . import routes
from helpers import sessionMaker
from database_setup import Restaurant, MenuItem

session = sessionMaker.newSession()


@routes.route("/restaurant/<int:restaurant_id>")
def showRestaurant(restaurant_id):
    restaurant = session.query(
        Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant_id)
    return render_template('menu.html', restaurant=restaurant,
                           items=items, restaurant_id=restaurant_id)


@routes.route("/restaurant/<int:restaurant_id>/JSON")
def showRestaurantJSON(restaurant_id):
    items = session.query(MenuItem).filter_by(
        restaurant_id=restaurant_id).all()
    return jsonify(MenuItems=[i.serialize for i in items])

from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

app = Flask(__name__)

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
def homepage():
    return "Welcome"


@app.route('/restaurants/<int:restaurant_id>/')
def restaurantMenu(restaurant_id):
    try:
        restaurant = session.query(
            Restaurant).filter_by(id=restaurant_id).one()
        items = session.query(MenuItem).filter_by(restaurant_id=restaurant.id)
        output = ''
        for i in items:
            output += i.name
            output += '</br>'
            output += i.price
            output += '</br>'
            output += i.description
            output += '</br>'
            output += '</br>'
        return output
    except:
        return "No restaurant found"


# Task 1: Create route for newMenuItem function here
@app.route('/restaurants/<int:restaurant_id>/new-menu-item/', methods=['GET', 'POST'])
def newMenuItem(restaurant_id):
    # How can I use a try/except block better here?
    if request.method == 'POST':
        newItem = MenuItem(name=request.form[
            'name'], restaurant_id=restaurant_id)
        session.add(newItem)
        session.commit()
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    else:
        return render_template('newmenuitem.html', restaurant_id=restaurant_id)


# Task 2: Create route for editMenuItem function here
@app.route('/restaurants/<int:restaurant_id>/edit-menu-item/<int:menu_id>/')
def editMenuItem(restaurant_id, menu_id):
    try:
        """
        restaurant = session.query(
            Restaurant).filter_by(id=restaurant.id).one()

        menuitem = session.query(
            Restaurant).filter_by(id=menu_id, restaurant_id=restaurant.id).one()
        """
        return "page to edit a menu item. Task 2 complete!"
    except:
        return "No restaurant or item found"


# Task 3: Create a route for deleteMenuItem function here
@app.route('/restaurants/<int:restaurant_id>/delete-menu-item/<int:menu_id>/')
def deleteMenuItem(restaurant_id, menu_id):
    try:
        return "page to delete a menu item. Task 3 complete!"
    except:
        return "No restaurant or item found"


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)

from . import bp as app
from flask import render_template, request, redirect, url_for, flash
from app.blueprints.main.models import User, Post, Car
from app import db
from flask_login import current_user, login_required

# Routes that return/display HTML

@app.route('/')
@login_required
def home():
    posts = Post.query.all()
    return render_template('home.html', user=current_user, posts=posts)

@app.route('/cars')
@login_required
def cars():
    cars = Car.query.all()
    return render_template('cars.html', user=current_user, cars=cars)

@app.route('/about')
@login_required
def about():
    return render_template('about.html')

@app.route('/contact')
@login_required
def contact():
    return render_template('contact.html')

@app.route('/post', methods=['POST'])
@login_required
def create_post():
    post_title = request.form['title']
    post_body = request.form['body']
    
    new_post = Post(title=post_title, body=post_body, user_id=current_user.id)

    db.session.add(new_post)
    db.session.commit()

    flash('Post added successfully', 'success')
    return redirect(url_for('main.home'))

@app.route('/post/<id>')
def post(id):
    single_post = Post.query.get(id)
    return render_template('single-post.html', post=single_post)

#route to see listed car

@app.route('/listing', methods=['POST'])
@login_required
def create_listing():
    listing_make = request.form['make']
    listing_model = request.form['model']
    lising_year = request.form['year']
    listing_color = request.form['color']
    listing_price = request.form['price']
    
    new_listing = Car(make=listing_make, model=listing_model, year=lising_year, color=listing_color, price=listing_price, user_id=current_user.id)

    db.session.add(new_listing)
    db.session.commit()

    flash('Listing added successfully', 'success')
    return redirect(url_for('main.cars'))

@app.route('/listing/<id>')
def listing(id):
    listedcar = Car.query.get(id)
    return render_template('list_car.html', listing=listedcar)
from flask import Blueprint, render_template, request
from .search import product_search
view = Blueprint('view', __name__)


@view.route('/')
def home():
    return render_template("home.html")

@view.route('/search', methods=['GET','POST'])
def search():
    user_query = request.args.get('q')  # Assuming the query is passed as a query parameter
    # products = get_product_attributes()  # Replace with your actual product attributes

    recommended_products = product_search(user_query)

    # Render a template or return the recommended products as a response
    return render_template('search_results.html', products=recommended_products)
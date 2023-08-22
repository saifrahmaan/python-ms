from flask import Blueprint, render_template, request
from .search import product_search, word2vec_search
view = Blueprint('view', __name__)


@view.route('/')
def home():
    return render_template("home.html")

@view.route('/search', methods=['GET','POST'])
def search():
    user_query = request.args.get('q')  # Assuming the query is passed as a query parameter

    recommended_products = word2vec_search(user_query)

    return render_template('search_results.html', products=recommended_products)
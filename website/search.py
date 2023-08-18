from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from .models import Products
# from gensim.models import Word2Vec
from sklearn.metrics.pairwise import cosine_similarity
# import os
# import numpy as np
from gensim.models.keyedvectors import KeyedVectors

word2vec_model_path = '/Users/saifrahman/Downloads/GoogleNews-vectors-negative300.bin'
word2vec_model = KeyedVectors.load_word2vec_format(word2vec_model_path, binary=True)

# word2vec_vectors_path = os.path.expanduser('~Users/saifrahman/Downloads/word2vec-google-news-300.model.vectors.npy') 
# word2vec_model.vectors = np.load(word2vec_vectors_path)

def product_search(query):
    products = get_product_attributes()  # Retrieve all product attributes

    # Extract text attributes for TF-IDF calculation
    product_descriptions = [product['short_details'] + ' ' + product['details'] for product in products]

    # Initialize and fit TF-IDF vectorizer
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(product_descriptions)

    # Transform the user query
    query_vector = tfidf_vectorizer.transform([query])

    # Calculate cosine similarity between query vector and product vectors
    cosine_similarities = linear_kernel(query_vector, tfidf_matrix).flatten()

    # Get indices of top recommendations
    top_indices = cosine_similarities.argsort()[::-1][:10]  # Adjust the number of recommendations

    # Return top recommended products
    recommended_products = [products[i] for i in top_indices]
    return recommended_products

def get_product_attributes():
    products = Products.query.all()  # Retrieve all products from the database
    product_attributes = []

    for product in products:
        product_info = {
            "id": product.id,
            "sku": product.sku,
            "name": product.name,
            "short_details": product.short_details,
            "details": product.details,
            "stock": product.stock,
            "price": product.price,
            "discount": product.discount,
            "lat_long": product.lat_long,
            "delivery_type": product.delivery_type,
            "stock_check_number": product.stock_check_number,
            "thumbnail_image": product.thumbnail_image,
            "seller_id": product.seller_id,
            "rating": product.rating,
            "verified": product.verified,
            "verification_status": product.verification_status,
            "comment": product.comment,
            "approved_by": product.approved_by,
            "created_at": product.created_at,
            "updated_at": product.updated_at
        }
        product_attributes.append(product_info)

    return product_attributes

def word2vec_search(query):
    # Get product descriptions and convert to word vectors
    products = get_product_attributes()
    product_descriptions = [product['short_details'] + ' ' + product['details'] for product in products]
    product_vectors = [get_average_word_vector(desc, word2vec_model) for desc in product_descriptions]

    # Convert user query to word vector
    user_query_vector = get_average_word_vector(query, word2vec_model)

    # Calculate cosine similarities between query vector and product vectors
    similarities = cosine_similarity([user_query_vector], product_vectors)

    # Sort products based on similarity
    sorted_indices = similarities.argsort()[0][::-1]
    recommended_products = [products[i] for i in sorted_indices[:10]]  # Top 10 recommendations

    return recommended_products

def get_average_word_vector(text, word2vec_model):
    words = text.lower().split()
    vectors = [word2vec_model[word] for word in words if word in word2vec_model]
    if not vectors:
        return None
    return sum(vectors) / len(vectors)

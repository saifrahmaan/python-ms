from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from .models import Products
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

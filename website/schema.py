import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from .models import Note, User, Products
from .search import product_search, word2vec_search

class ProductSearchResult(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String()
    price = graphene.Float()

class NoteType(SQLAlchemyObjectType):
    class Meta:
        model = Note

class UserType(SQLAlchemyObjectType):
    class Meta:
        model = User

class ProductType(SQLAlchemyObjectType):
    class Meta:
        model = Products

class Query(graphene.ObjectType):
    notes = graphene.List(NoteType)
    users = graphene.List(UserType)
    products = graphene.List(ProductType, name = graphene.String())

    def resolve_notes(self, info):
        return Note.query.all()

    def resolve_users(self, info):
        return User.query.all()

    def resolve_products(self, info, name=None):
        if name:
            return Products.query.filter_by(name=name).all()
        else:
            return Products.query.all()
    
    tfidf_product_search = graphene.List(ProductType, query=graphene.String())
    word2vec_product_search = graphene.List(ProductType, query=graphene.String())

    search_products = graphene.List(ProductSearchResult, query=graphene.String())

    def resolve_tfidf_product_search(self, info, query):
        return product_search(query)

    def resolve_word2vec_product_search(self, info, query):
        return word2vec_search(query)
    
    def resolve_search_products(self, info, query):
        tfidf_results = product_search(query)
        word2vec_results = word2vec_search(query)
        
        # Combine and return the search results
        search_results = tfidf_results + word2vec_results
        return search_results

schema = graphene.Schema(query=Query)
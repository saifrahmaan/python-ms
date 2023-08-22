from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import JSON  # Import JSON type

db = SQLAlchemy()

class Note(db.Model):
    id = db.Column(db.Integer , primary_key= True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), server_default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer , primary_key= True)
    email= db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')

class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sku = db.Column(db.String(255))
    name = db.Column(db.String(255))
    short_details = db.Column(db.Text)
    details = db.Column(db.Text)
    stock = db.Column(db.BigInteger)
    price = db.Column(db.BigInteger)
    discount = db.Column(db.BigInteger)
    lat_long = db.Column(JSON)  # JSON field
    delivery_type = db.Column(JSON)  # JSON field
    stock_check_number = db.Column(db.String(255))
    thumbnail_image = db.Column(db.String(255))
    seller_id = db.Column(db.BigInteger)
    rating = db.Column(db.Float)
    verified = db.Column(db.Boolean)
    verification_status = db.Column(db.String(255))
    comment = db.Column(db.String(255))
    approved_by = db.Column(db.BigInteger)
    created_at = db.Column(db.TIMESTAMP(timezone=True))
    updated_at = db.Column(db.TIMESTAMP(timezone=True))
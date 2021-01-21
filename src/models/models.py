import os
from flask_migrate import Migrate
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

# Declare database name
database_name = "filed"

# initiate db with no assignment
db = SQLAlchemy()


# function is used to bend our app with the database
def setup_db(app, database_name):
    app.config.from_pyfile('config.py')
    app.config[ 'SQLALCHEMY_DATABASE_URI' ] += database_name
    moment = Moment(app)
    db.app = app
    db.init_app(app)
    # create instance migrate for data migration
    migrate = Migrate(app, db, compare_type=True)


# Premium Payment Gateway table
class PremiumPayment(db.Model):
    __tablename__ = 'premium_payment'

    id = db.Column(db.Integer, primary_key=True)
    credit_card_number = db.Column(db.String(), nullable=False)
    card_holder = db.Column(db.String(), nullable=False)
    expiration_date = db.Column(db.DateTime(), nullable=False)
    security_code = db.Column(db.String(32))
    amount = db.Column(db.Float, nullable=False)

    def __init__(self, credit_card_number, card_holder, expiration_date, security_code, amount):
        self.credit_card_number = credit_card_number
        self.card_holder = card_holder
        self.expiration_date = expiration_date
        self.security_code = security_code
        self.amount = amount

    def insert(self):
        db.session.add(self)
        db.session.commit()


# Expensive Payment Gateway table
class ExpensivePayment(db.Model):
    __tablename__ = 'expensive_payment'

    id = db.Column(db.Integer, primary_key=True)
    credit_card_number = db.Column(db.String(), nullable=False)
    card_holder = db.Column(db.String(), nullable=False)
    expiration_date = db.Column(db.DateTime(), nullable=False)
    security_code = db.Column(db.String(32))
    amount = db.Column(db.Float, nullable=False)

    def __init__(self, credit_card_number, card_holder, expiration_date, security_code, amount):
        self.credit_card_number = credit_card_number
        self.card_holder = card_holder
        self.expiration_date = expiration_date
        self.security_code = security_code
        self.amount = amount

    def insert(self):
        db.session.add(self)
        db.session.commit()


# Cheap Payment Gateway table
class CheapPayment(db.Model):
    __tablename__ = 'cheap_payment'

    id = db.Column(db.Integer, primary_key=True)
    credit_card_number = db.Column(db.String(), nullable=False)
    card_holder = db.Column(db.String(), nullable=False)
    expiration_date = db.Column(db.DateTime(), nullable=False)
    security_code = db.Column(db.String(32))
    amount = db.Column(db.Float, nullable=False)

    def __init__(self, credit_card_number, card_holder, expiration_date, security_code, amount):
        self.credit_card_number = credit_card_number
        self.card_holder = card_holder
        self.expiration_date = expiration_date
        self.security_code = security_code
        self.amount = amount

    def insert(self):
        db.session.add(self)
        db.session.commit()

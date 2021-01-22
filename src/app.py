# ----------------------------------------------------------------------------#
# Imports
# ----------------------------------------------------------------------------#

from flask import Flask, request, jsonify, abort
from flask_cors import CORS
from .make_payments import *
from datetime import datetime
from .validiator import validate


# creating and initializing the app.
def create_app():
    # ----------------------------------------------------------------------------#
    # App Config.
    # ----------------------------------------------------------------------------#
    app = Flask(__name__)
    # wrap database to app
    setup_db(app, database_name)
    # using cors with app
    CORS(app)

    # CORS Headers
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        return response

    # enable testing
    app.testing = True

    # ----------------------------------------------------------------------------#
    # payment end point.
    # CreditCardNumber (mandatory, string, it should be a valid credit card number)
    # CardHolder: (mandatory, string)
    # ExpirationDate (mandatory, DateTime, it cannot be in the past)
    # SecurityCode (optional, string, 3 digits)
    # Amount (mandatory decimal, positive amount)
    # ----------------------------------------------------------------------------#

    @app.route('/payment', methods=[ 'POST' ])
    def ProcessPayment():
        body = request.get_json()

        # check if credit card number is valid
        credit_card_number = body.get('CreditCardNumber', None)
        if credit_card_number:
            if not validate(credit_card_number):
                abort(400)
        else:
            abort(400)

        # check card holder provided
        card_holder = body.get('CardHolder', None)
        if not card_holder:
            abort(400)

        # check if expiration_date older than current date
        expiration_date = body.get('ExpirationDate', None)
        if expiration_date:
            expiration_date_format = datetime.strptime(expiration_date, '%Y-%m-%d %H:%M:%S.%f')
            if expiration_date_format <= datetime.now():
                abort(400)
        else:
            abort(400)
        # security code is optional
        security_code = body.get('SecurityCode', None)
        # check amount to be positive and not none
        amount = body.get('Amount', None)
        if not amount or amount<0:
            abort(400)

        data = {
            'credit_card_number': credit_card_number,
            'card_holder': card_holder,
            'expiration_date': expiration_date,
            'security_code': security_code,
            'amount': amount
        }
        try:
            status = make_payments(data)
            if status[ 'success' ]:
                return jsonify({
                    'success': True,
                    'message': 'Payment is processed'
                })


        except Exception as e:
            abort(500)

    # ----------------------------------------------------------------------------#
    # Error Handlers.
    # ----------------------------------------------------------------------------#

    @app.errorhandler(400)
    def not_good_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": 'Bad Request!!!! Please make sure the data you entered is correct'
        }), 400

    @app.errorhandler(500)
    def server_error(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": 'Internal Server Error!!!: Please try again later or reload request. '
        }), 500

    return app

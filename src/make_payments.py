from .payment_gateways import ExpensivePaymentGateway, PremiumPaymentGateway, CheapPaymentGateway
from flask import abort, jsonify

cc = 5104740265868658


def make_payments(data):
    if 0 < data['amount'] < 21:
        try:
            status = CheapPaymentGateway(data)
            if status['success']:
                return jsonify({
                    "success": True,
                    "message": 'Payment is processed'
                })
        except:
            abort(500)
    elif 21 <= data['amount'] <= 500:
        try:
            ExpensivePaymentGateway(data)
        except:
            try:
                CheapPaymentGateway(data)
            except:
                abort(500)
    elif data['amount'] > 500:

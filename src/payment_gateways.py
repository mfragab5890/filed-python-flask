from .models.models import *


# PremiumPaymentGateway
def PremiumPaymentGateway(data):
    try:
        payment = PremiumPayment(
            credit_card_number=data['credit_card_number'],
            card_holder=data['card_holder'],
            expiration_date=data['expiration_date'],
            security_code=data['security_code'],
            amount=data['amount']
        )
        payment.insert()
        return {
            "success": True,
            "message": 'Payment Details Sent Successfully'
        }
    except:
        return {
            "success": False,
            "message": 'Payment Unsuccessful'
        }


# ExpensivePaymentGateway
def ExpensivePaymentGateway(data):
    try:
        payment = ExpensivePayment(
            credit_card_number=data[ 'credit_card_number' ],
            card_holder=data[ 'card_holder' ],
            expiration_date=data[ 'expiration_date' ],
            security_code=data[ 'security_code' ],
            amount=data[ 'amount' ]
        )
        payment.insert()
        return {
            "success": True,
            "message": 'Payment Details Sent Successfully'
        }
    except:
        return {
            "success": False,
            "message": 'Payment Unsuccessful'
        }


# CheapPaymentGateway
def CheapPaymentGateway(data):
    try:
        payment = CheapPayment(
            credit_card_number=data[ 'credit_card_number' ],
            card_holder=data[ 'card_holder' ],
            expiration_date=data[ 'expiration_date' ],
            security_code=data[ 'security_code' ],
            amount=data[ 'amount' ]
        )
        payment.insert()
        return {
            "success": True,
            "message": 'Payment Details Sent Successfully'
        }
    except:
        return {
            "success": False,
            "message": 'Payment Unsuccessful'
        }

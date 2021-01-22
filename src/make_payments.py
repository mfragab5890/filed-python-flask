from .payment_gateways import *
from flask import abort


# make payment according to business rules
def make_payments(data):
    # first check payment type
    if 0 < data[ 'amount' ] < 21:
        try:
            # try only once
            status = CheapPaymentGateway(data)
            if status[ 'success' ]:
                return {
                    "success": True,
                    "message": 'Payment is processed'
                }
        except:
            abort(500)
    elif 21 <= data[ 'amount' ] <= 500:
        try:
            # try expensive if failed then try cheap payment
            status = ExpensivePaymentGateway(data)
            if status[ 'success' ]:
                return {
                    "success": True,
                    "message": 'Payment is processed'
                }
        except:
            try:
                # try cheap payment upon expensive payment failure
                status = CheapPaymentGateway(data)
                if status[ 'success' ]:
                    return {
                        "success": True,
                        "message": 'Payment is processed'
                    }
            except:
                abort(500)

    elif data[ 'amount' ] > 500:
        try:
            # try premium payment once
            status = PremiumPaymentGateway(data)
            if status[ 'success' ]:
                return {
                    "success": True,
                    "message": 'Payment is processed'
                }
        except:
            trials = 0
            fail = False
            # try premium payment three times more upon first trial failure
            while trials < 3:
                status = PremiumPaymentGateway(data)
                if status[ 'success' ]:
                    trials += 3
                    return {
                        "success": True,
                        "message": 'Payment is processed'
                    }
                else:
                    trials += 1
                    if trials == 3:
                        fail = True
            if fail:
                abort(500)
    else:
        abort(400)
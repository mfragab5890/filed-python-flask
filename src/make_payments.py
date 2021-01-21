from .payment_gateways import ExpensivePaymentGateway, PremiumPaymentGateway, CheapPaymentGateway
cc = 5104740265868658
def make_payments(data):
    if 21 > data.amount > 0:
        try:
            CheapPaymentGateway(data)
        except:

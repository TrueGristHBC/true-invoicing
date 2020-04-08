import stripe

class InvoiceItem:
    def __init__(self, currency='cad', description=None, quantity=1, unit_amount=0):
        self._currency = currency
        self._description = description
        self._quantity = quantity
        self._unit_amount = unit_amount

    @property
    def customer(self):
        return self._customer_id

    @property
    def currency(self):
        return self._currency

    @property
    def description(self):
        return self._description

    @property
    def quantity(self):
        return self._quantity

    @property
    def unit_amount(self):
        return self._unit_amount


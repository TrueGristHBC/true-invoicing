import stripe

class Invoice:
    def __init__(self, collection_method="send_invoice", days_until_due=7, description=None):
        self._collection_method = collection_method
        self._days_until_due = days_until_due
        self._description = description

    @property
    def collection_method(self):
        return self._collection_method

    @property
    def customer(self):
        return self._customer

    @property
    def days_until_due(self):
        return self._days_until_due

    @property
    def description(self):
        return self._description



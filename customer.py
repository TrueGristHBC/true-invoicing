import stripe

class Customer:
    def __init__(self, email=None, username=None, name=None):
        self._email = email
        self._username = username
        self._name = name

    def fetch(self):
        if self._email is None:
            print('User email is not defined. Did not fetch customer.')
            return False

        tmp_id = self.get_customer_id(self._email)

        if tmp_id is None:
            return False

        self._id = tmp_id

        r = stripe.Customer.retrieve(self._id)
        if r is None:
            return False

        self._account_balance = r.get('account_balance')
        self._balance = r.get('balance')
        self._name = r.get('name')
        try:
            self._username = r.get('metadata').get('username')
        except:
            self._username = ''

    def post(self):
        pass

    def info(self):
        print('id: {}'.format(self._id))
        print('name: {}'.format(self._name))
        print('email: {}'.format(self._email))
        print('username: {}'.format(self._username))
        print('account_balance: {}'.format(self._account_balance))
        print('balance: {}'.format(self._balance))

    def set_info(self, name=None, email=None, username=None):
        if name is not None:
            self._name = name
        if email is not None:
            self._email = email
        if username is not None:
            self._username = username

    @staticmethod
    def get_customer_id(email):
        try:
            for c in stripe.Customer.list():
                if c.get('email').lower() == email.lower():
                    return c.get('id')
        except:
            print('Issue with get_customer_id email lookup')

        print('could not find customer with email: {}'.format(email))
        return None

    @property
    def account_balance(self):
        return self._account_balance

    @property
    def balance(self):
        return self._balance

    @property
    def email(self):
        return self._email

    @property
    def id(self):
        return self._id

    @property
    def username(self):
        return self._username

    @property
    def name(self):
        return self._name
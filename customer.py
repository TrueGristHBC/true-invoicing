import stripe

class Customer:
    '''
    The Customer object contains information about a customer and interacts with stripe via api

    Args:
        email (str): customer email
        username (str): customer username
        name (str): customer name

    Attributes:
        account_balance (int): customer account balance in cents
        balance (int): customer balance in cents
        email (str): email the customer is linked to, acts as unique id
        id (str): id of customer in API interaction
        name (str): customer name
        username (str): website username. Interacts with API metadata
    '''
    def __init__(self, email=None, username=None, name=None):
        self._email = email
        self._username = username
        self._name = name

    def retrieve(self):
        '''
        Retrieve the user using API based on email. Will fail if email doesn't exist.

        Returns:
            passed: whether retrieval succeeded
        '''
        #we check to see if email is defined as we use that as our customer ID
        if self._email is None:
            print('User email is not defined. Did not fetch customer.')
            return False

        # Search through the list of customers for that email
        # if we find it, set the custome id to that id
        tmp_id = self.get_customer_id(self._email)

        if tmp_id is None:
            return False

        self._id = tmp_id

        # Try to retrieve the customer from the API, if anything goes wrong return false
        try:
            r = stripe.Customer.retrieve(self._id)
        except:
            print('API error')
            return False

        if r is None:
            return False

        # Update the customer object based on API call
        self._account_balance = r.get('account_balance')
        self._balance = r.get('balance')
        self._name = r.get('name')
        try:
            self._username = r.get('metadata').get('username')
        except:
            self._username = ''

    def update(self):
        '''
        Update the user using API based on email. Will fail if user id hasn't been set yet.

        Returns:
            passed: whether update succeeded
        '''
        if self._id is None:
            print('No id associated with this customer')
            return False
        try:
            stripe.Customer.modify(self._id,
                                   email=self._email,
                                   metadata={'username': self._username},
                                   name=self._name)
            return True
        except:
            print('Error with API request')
            return False

    def create(self):
        '''
        Create the user on server using API based on email. Will fail if email doesn't exist.

        Returns:
            passed: whether creation succeeded
        '''
        if self._email is None:
            print('No email associated with this customer. Cannot create.')
            return False

        # check to see if this email is already associated with someone
        tmp_id = self.get_customer_id(self._email, verbose=False)
        if tmp_id is not None:
            print('Customer with id {} already exists'.format(tmp_id))
            return False

        stripe.Customer.create(email=self._email,
                                metadata={'username': self._username},
                                name=self._name)
        return True




    def info(self):
        '''
        Print the info associated with the Customer object.
        '''
        print('id: {}'.format(self._id))
        print('name: {}'.format(self._name))
        print('email: {}'.format(self._email))
        print('username: {}'.format(self._username))
        print('account_balance: {}'.format(self._account_balance))
        print('balance: {}'.format(self._balance))

    def set_info(self, name=None, email=None, username=None):
        '''
        Set the info for the customer object. Allows modification before update or creation on the API server.

        Args:
            name (str): The name of the customer
            email (str): The email of the customer
            username (str): The username of the customer
        '''
        if name is not None:
            self._name = name
        if email is not None:
            self._email = email
        if username is not None:
            self._username = username

    @staticmethod
    def get_customer_id(email, verbose=True):
        '''
        Attempt to get the customer id based on email address from the API server

        Args:
            email (str): The customer email
            verbose (bool): Whether to print basic logic errors

        Returns:
            id: customer id
        '''
        try:
            for c in stripe.Customer.list():
                if c.get('email').lower() == email.lower():
                    return c.get('id')
        except:
            print('Issue with get_customer_id email lookup')

        if verbose:
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
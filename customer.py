import stripe

def get_customer_id(email):
    customer_list = stripe.Customer.list()

    try:
        for c in customer_list:
            if c.get('email').lower() == email.lower():
                return c.get('id')
    except:
        print('Issue with get_customer_id email lookup')

    return None



def find_customer(id):
    print(stripe.Customer.retrieve(id))
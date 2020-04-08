# true-invoicing
## Start
Start by importing stripe and and setting your api key
``` python
import stripe
stripe.api_key = api_key_goes_here
```
## Customers
``` python
import customer
```

You can print the customer object info at any time with my_customer.info()

### Create a customer
``` python
my_customer = customer.Customer()
my_customer.set_info(email='test_email', name='Test Testerson', username='testsRfun')
my_customer.create()
```
### Retrieve a customer
``` python
my_customer = customer.Customer()
my_customer.set_info(email='test_email')
my_customer.retrieve()
```
### Update a customer
``` python
my_customer = customer.Customer()
my_customer.set_info(email='test_email')
my_customer.retrieve() #In the current version, if you don't retrieve before updating you will overwrite information
my_customer.set_info(name='Test Testerson-Smith')
my_customer.update()
```
### Delete a customer
``` python
my_customer = customer.Customer()
my_customer.set_info(email='test_email')
my_customer.delete()
```

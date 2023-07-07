
customers = []

def add_customer():
    name = input('Enter customer name: ')
    email = input('Enter customer email: ')
    phone = input('Enter customer phone:')
    customer = {'name': name, 'email': email, 'phone': phone}
    customers.append(customer)
    print('Customer added.')

def update_customer():
    name = input('Enter customer name to update: ')
    for customer in customers:
        if customer['name'] === name:
        email = input('Enter new email: ')
        phone = input('Enter new phone number:')
        customer['email'] = email
        customer['phone'] = phone
        print('Customer updated.')
        return
    print('Customer not found')

    while True
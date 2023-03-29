print('Davy\'s auto shop services\nOil change -- $35\nTire rotation -- $19\nCar wash -- $7\nCar wax -- $12')

service1 = input('\nSelect first service:')
service2 = input('\nSelect second service:')

print('\n\nDavy\'s auto shop invoice\n')

services = {'Oil change':35, 'Tire rotation':19, 'Car wash':7, 'Car wax':12}

if service1 in services:
    if service1 == 'Oil change':
        print(f'Service 1: Oil change, ${services["Oil change"]}')
        total = services["Oil change"]
    elif service1 == 'Tire rotation':
        print(f'Service 1: Tire rotation, ${services["Tire rotation"]}')
        total = services["Tire rotation"]
    elif service1 == 'Car wash':
        print(f'Service 1: Car wash, ${services["Car wash"]}')
        total = services["Car wash"]
    elif service1 == 'Car wax':
        print(f'Service 1: Car wax, ${services["Car wax"]}')
        total = services["Car wax"]
else:
    print('Service 1: No service')
    total = 0

if service2 in services:
    if service2 == 'Oil change':
        print(f'Service 2: Oil change, ${services["Oil change"]}')
        new_total = total + services["Oil change"]
    elif service2 == 'Tire rotation':
        print(f'Service 2: Tire rotation, ${services["Tire rotation"]}')
        new_total = total + services["Tire rotation"]
    elif service2 == 'Car wash':
        print(f'Service 2: Car wash, ${services["Car wash"]}')
        new_total = total + services["Car wash"]
    elif service2 == 'Car wax':
        print(f'Service 2: Car wax, ${services["Car wax"]}')
        new_total = total + services["Car wax"]
else:
    print('Service 2: No service')
    new_total = total + 0

print(f'\nTotal: ${new_total}')
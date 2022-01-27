#basic hash table implementation using a hash function


def hash_key( key, m):
    return key % m


m = 7

print(f'The hash value for 3 is {hash_key(3,m)}')
print(f'The hash value for 2 is {hash_key(2,m)}')
print(f'The hash value for 9 is {hash_key(9,m)}')
print(f'The hash value for 11 is {hash_key(11,m)}')
print(f'The hash value for 7 is {hash_key(7,m)}')
print("\n")
#using python dictionary

employee = {
    'name': 'Raja',
    'age': 22,
    'position': 'F1 race engineer.'
}

print (f"The name of the employee is {employee['name']}")
employee['position'] = 'Data Engineer'
print (f"The position of {employee['name']} is {employee['position']}")
employee.clear()

print (employee)


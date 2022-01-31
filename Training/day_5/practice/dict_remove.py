#while using dictionary 
# 1 
# using del

# Initializing dictionary
test_dict = {"Arushi" : 22, "Anuradha" : 21, "Mani" : 21, "Haritha" : 21}

# Printing dictionary before removal
print ("The dictionary before performing remove is : " + str(test_dict))

# Using del to remove a dict
# removes Mani
del test_dict['Mani']

# Printing dictionary after removal
print ("The dictionary after remove is : " + str(test_dict))



# Using del to remove a dict
# raises exception
del test_dict['Manjeet']

#2
# using pop()

# Initializing dictionary
test_dict = {"Arushi" : 22, "Anuradha" : 21, "Mani" : 21, "Haritha" : 21}

# Printing dictionary before removal
print ("The dictionary before performing remove is : " + str(test_dict))

# Using pop() to remove a dict. pair
# removes Mani
removed_value = test_dict.pop('Mani')

# Printing dictionary after removal
print ("The dictionary after remove is : " + str(test_dict))
print ("The removed key's value is : " + str(removed_value))

print ('\r')

# Using pop() to remove a dict. pair
# doesn't raise exception
# assigns 'No Key found' to removed_value
removed_value = test_dict.pop('Manjeet', 'No Key found')

# Printing dictionary after removal
print ("The dictionary after remove is : " + str(test_dict))
print ("The removed key's value is : " + str(removed_value))

#3
# using items() + dict comprehension

# Initializing dictionary
test_dict = {"Arushi" : 22, "Anuradha" : 21, "Mani" : 21, "Haritha" : 21}

# Printing dictionary before removal
print ("The dictionary before performing remove is : " + str(test_dict))

# Using items() + dict comprehension to remove a dict. pair
# removes Mani
new_dict = {key:val for key, val in test_dict.items() if key != 'Mani'}

# Printing dictionary after removal
print ("The dictionary after remove is : " + str(new_dict))

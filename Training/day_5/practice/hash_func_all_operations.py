#creating empty hash table
hash_table = [[] for _ in range(10)]
print("Hash table creation: ")
print (hash_table)
print("\n")

#insert data into hash table
def insert(hash_table, key, value):
	hash_key = hash(key) % len(hash_table)
	key_exists = False
	bucket = hash_table[hash_key]	
	for i, kv in enumerate(bucket):
		k, v = kv
		if key == k:
			key_exists = True 
			break
	if key_exists:
		bucket[i] = ((key, value))
	else:
		bucket.append((key, value))

print("insert to hash table :")
insert(hash_table, 10, 'Nepal')
insert(hash_table, 25, 'USA')
insert(hash_table, 20, 'India')
print (hash_table)
print("\n")

#Search data in hash table
def search(hash_table, key):
	hash_key = hash(key) % len(hash_table)	
	bucket = hash_table[hash_key]
	for i, kv in enumerate(bucket):
		k, v = kv
		if key == k:
			return v

print("Search:")
print (search(hash_table, 10))
print (search(hash_table, 20)) 
print (search(hash_table, 30)) 
print("\n")
#delete data from hash table
def delete(hash_table, key):
	hash_key = hash(key) % len(hash_table)	
	key_exists = False
	bucket = hash_table[hash_key]
	for i, kv in enumerate(bucket):
		k, v = kv 
		if key == k:
			key_exists = True 
			break
	if key_exists:
		del bucket[i]
		print ('Key {} deleted'.format(key))
	else:
		print ('Key {} not found'.format(key))

print("Delete from hash table:")
delete(hash_table, 100)
print (hash_table)

delete(hash_table, 10)
print (hash_table)

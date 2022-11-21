
import hashlib

# prints all available algorithms
print ("The available algorithms are : ", end ="")
print (hashlib.algorithms_guaranteed)

#Encryption using sha1
string = 'abc'
res = hashlib.sha1(string.encode())
print(res.hexdigest())
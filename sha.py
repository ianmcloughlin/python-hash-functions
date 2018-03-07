# https://www.pythoncentral.io/hashing-strings-with-python/	
import hashlib

# Available algorithms
print(hashlib.algorithms_available)
print(hashlib.algorithms_guaranteed)

# MD5
hash_object = hashlib.md5(b'Hello World')
print(hash_object.hexdigest())

# MD5 from user
mystring = input('Enter String to hash: ')
# Assumes the default UTF-8
hash_object = hashlib.md5(mystring.encode())
print(hash_object.hexdigest())


# SHA1
hash_object = hashlib.sha1(b'Hello World')
hex_dig = hash_object.hexdigest()
print(hex_dig)


# SHA224
hash_object = hashlib.sha224(b'Hello World')
hex_dig = hash_object.hexdigest()
print(hex_dig)

# SHA256
hash_object = hashlib.sha256(b'Hello World')
hex_dig = hash_object.hexdigest()
print(hex_dig)

# SHA384
hash_object = hashlib.sha384(b'Hello World')
hex_dig = hash_object.hexdigest()
print(hex_dig)

# SHA512
hash_object = hashlib.sha512(b'Hello World')
hex_dig = hash_object.hexdigest()
print(hex_dig)

# OpenSSL
hash_object = hashlib.new('DSA')
hash_object.update(b'Hello World')
print(hash_object.hexdigest())

# Passwords
import uuid
import hashlib
 
def hash_password(password):
  # uuid is used to generate a random number
  salt = uuid.uuid4().hex
  return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt
    
def check_password(hashed_password, user_password):
  password, salt = hashed_password.split(':')
  return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()
 
new_pass = input('Please enter a password: ')
hashed_password = hash_password(new_pass)
print('The string to store in the db is: ' + hashed_password)
old_pass = input('Now please enter the password again to check: ')
if check_password(hashed_password, old_pass):
  print('You entered the right password')
else:
  print('I am sorry but the password does not match')
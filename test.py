from utilities.Auth import *

print(Auth.valid_password("123456"))
print(Auth.valid_password("123456A"))
print(Auth.valid_password("123456a"))
print(Auth.valid_password("123456AAa"))




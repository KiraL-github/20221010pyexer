from validator import validate_email
import validator
import camelcase
from time import time
import time
# from datetime import date
import datetime

# Core modules are the python build in modules

# pip modules
# pip install camelcase
# without installing camelcase, you run into errors
# pip freeze to check the module installed or not

# Custom modules

today = datetime.date.today()
# today = date.today()
timestamp = time()
print(today, timestamp)
text = 'hello there world'
camel = camelcase.CamelCase()

print(camel.hump(text))

email = 'test@test.com'
if validate_email(email):
    print('Email is valid')
else:
    print('Not an email')

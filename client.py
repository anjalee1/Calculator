import requests

import json
operator=input('''Type one of the opertaors from these options:
                 + : For addition
                 - : For substraction
                 * : For multiplication
                 / : For Divison

                 Type here: ''')

num1 =int(input('Enter First Number:'))
num2=int(input('Enter Second Number:'))
data={'operator':'','num1':'','num2':''}
data['operator']=operator
data['num1']=num1
data['num2']=num2
r1=requests.post(url='http://localhost:8080/',data=json.dumps(data))
# r2=requests.get(url='http://localhost:8080/')

import requests
from requests.auth import HTTPBasicAuth
import json
import io
import csv

user = 'tal@solargik.com'
Apitoken = 'ATATT3xFfGF0pfP0KuIsaieqVTT9qpztQ7T-UV7Nb9cHmXCdo1INLVe8UblXK8dNngEtnxxygNsnb7Is62pdF9kfFzWIg9H-mY_N466aRem1LbMt1UpKwAPIQUZb3gpdrSUXDb1IWeSDyWAoxVFXHG8Fnp61l3Z-zC-ZX8iLdWItjFidfnNtYSw=A8DCA417'

url = "https://solargik.atlassian.net/rest/api/3/user"

# auth = HTTPBasicAuth("user", "Apitoken")

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

with io.open("userslist.csv", "r", encoding="utf-8") as f1:
    user_data = f1.read()
    f1.close()
user_data = user_data.split("\n")[1:]
print(user_data)
for users in user_data:
    #   displayName = users.split(",")[0]
    #    pwd = users.split(",")[1]
    emailAddress = users.split(",")[0]
#    name = users.split(",")[2]
payload = json.dumps(
    {
        "emailAddress": emailAddress
    }
)
response = requests.post(url, headers=headers, data=payload, auth=(user, Apitoken))
print(response.text)

# print(user_data)
# jira = JIRA('https://solargik.atlassian.net')

# auth_jira = JIRA(basic_auth=(user, Apitoken))

# jira.add_user('user1', 'user1@solargik.com', '12345', 'user1', False, True, False)

'''
 "displayName": "User One",
 "name": "UserOne"
 "password": "test@123",           
'''

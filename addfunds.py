import requests
import sys
import math
f = open('cookie.txt', 'r')
cookie = f.read()

totalFunds = math.ceil(int(sys.argv[2]) / 1000 )
accountid = sys.argv[1]
url = 'https://3commas.io/accounts/' + str(accountid) + '/papertrading_deposit'

headers = {
    'Cookie' : cookie,
}

for x in range(totalFunds):
    response = requests.post(url, headers=headers)
    print( response.content )

f.close()
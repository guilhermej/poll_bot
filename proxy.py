#####################################
# Python para Pentesters            #
# https://solyd.com.br/treinamentos #
#####################################

import requests

proxy = {'http': 'http://156.56.18.228:8080'}

header = {"user-agent": "Mozilla/5.0 (X11; Linux i686; rv:43.0) Gecko/20100101 Firefox/43.0 Iceweasel/43.0.4",
          }
url = 'http://meuip.eu/'

resposta = requests.get(url, headers=header)

print resposta.text

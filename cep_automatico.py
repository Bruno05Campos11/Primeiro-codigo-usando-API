import requests
import json

cep = int (input("Digite seu CEP: "))
url = str('https://viacep.com.br/ws/{}/json/')
url = url.format (cep)

try:
  endereco = requests.get (url, timeout = 3)
  endereco = endereco.json ()
except:
  print ("Não foi possível acessar a API, verifique a fonte do problema")

estado = str(endereco ['uf'])
cidade = str(endereco ['localidade'])

print (f"CEP digitado: {cep}\n estado: {estado}, cidade: {cidade}")

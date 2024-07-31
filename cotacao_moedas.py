#API's (Application Programming Interface)
import requests #biblioteca comumente usada para usar API's
import json #formato de texto compactado comumente usado para comunicação entre servidores

try:
  moedas = requests.get ("https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL", timeout = 3)
  moedas = moedas.json ()

  dolar = moedas ['USDBRL']
  dolar = dolar ['bid']
  print (f"O valor do dolar nesse exato momento é: R$ {float(dolar):.2f}")

  euro = moedas ['EURBRL']
  euro = euro ['bid']
  print (f"O valor do euro nesse exato momento é: R$ {float(euro):.2f}")

except:
  print ("Não foi possível acessar a API, verifique a fonte do problema")

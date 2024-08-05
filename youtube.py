#a chave de autentificação foi excluída e não poderá ser usada, crie uma nova para testar
from googleapiclient.discovery import build
chave_api = "AIzaSyB0kCjM91ldEDJ4kfGwtqWPGnhKkjG1ASc"
youtube = build('youtube','v3', developerKey=chave_api)
import json

pesquisa = youtube.search().list (q="one piece crítica", part = 'snippet', maxResults = 5, type="playlist").execute()
for item in pesquisa ['items']:
  print (f"Título da playlist: {item ['snippet']['title']}")
  print (f"Thumbnails: {item ['snippet']['thumbnails']}\n")

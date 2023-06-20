import requests

url = 'http://localhost:88/'

response = requests.get(url)

if response.status_code == 200:
    songs = response.json()
    for song in songs:
        wykonawca = song['wykonawca']
        tytuł = song['tytuł']
        format = song['format']
        print(f'Wykonawca: {wykonawca}, Tytuł: {tytuł}, Format: {format}')
else:
    print('Błąd podczas pobierania danych z serwera.')

import requests
import json


class ClientReceiver:
    def __init__(self, base_url):
        self.base_url = base_url

    def receive_project_data(self, project_id):
        endpoint = f'/get/{project_id}'
        url = self.base_url + endpoint

        response = requests.get(url)

        if response.status_code == 200:
            project_data = json.loads(response.text)
            print('Données du projet reçues avec succès:')
            print('Code du projet:', project_data.get('code_projet'))
            print('Description du projet:', project_data.get('description'))
        else:
            print('Erreur lors de la récupération des données de projet.')


if __name__ == '__main__':
    base_url = 'http://127.0.0.1:8000'
    client_receiver = ClientReceiver(base_url)

    project_id = input('ID du projet à récupérer : ')

    client_receiver.receive_project_data(project_id)

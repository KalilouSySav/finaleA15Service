import requests


class ClientSender:
    def __init__(self, base_url):
        self.base_url = base_url

    def send_project_data(self, code, description):
        endpoint = '/insert/'
        url = self.base_url + endpoint

        data = {
            'code_projet': code,
            'description': description
        }

        response = requests.post(url, data=data)

        if response.status_code == 200:
            print('Données de projet envoyées avec succès.')
        else:
            print('Erreur lors de l''envoi des données de projet.')


if __name__ == '__main__':
    base_url = 'http://127.0.0.1:8000'
    client_sender = ClientSender(base_url)

    code_projet = input('Code du projet : ')
    description = input('Description du projet : ')

    client_sender.send_project_data(code_projet, description)

import requests
import os

class EmailService:
    def simular_envio(self, caminho_arquivo):
        if not os.path.exists(caminho_arquivo):
            raise FileNotFoundError("Arquivo do relatório não encontrado.")

        payload = {
            "to": "avaliador@empresa.com",
            "subject": "Relatório de Média de Caracteres",
            "attachment": os.path.basename(caminho_arquivo)
        }

        response = requests.post("http://localhost:5000/send-email", json=payload)
        print("Resposta da API fictícia:", response.json())

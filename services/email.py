import requests
import os

class EmailService:
    """
    Serviço responsável por simular o envio de e-mails com anexos.
    """

    def simular_envio(self, caminho_arquivo):
        """
        Simula o envio de um e-mail com o relatório em anexo.

        Args:
            caminho_arquivo (str): Caminho para o arquivo do relatório a ser enviado.

        Raises:
            FileNotFoundError: Se o arquivo especificado não existir.

        Side effects:
            Faz uma requisição POST simulando o envio do e-mail.
            Imprime a resposta da API fictícia no console.
        """
        if not os.path.exists(caminho_arquivo):
            raise FileNotFoundError("Arquivo do relatório não encontrado.")

        payload = {
            "to": "avaliador@empresa.com",
            "subject": "Relatório de Média de Caracteres",
            "attachment": os.path.basename(caminho_arquivo)
        }

        response = requests.post("http://localhost:5000/send-email", json=payload)
        print("Resposta da API fictícia:", response.json())

import pandas as pd
import os

class ReportService:
    """
    Serviço responsável por gerar relatórios em formato Excel a partir de dados fornecidos.
    """

    def gerar_excel(self, dados, caminho_arquivo):
        """
        Gera um arquivo Excel com os dados informados.

        Args:
            dados (list[dict]): Lista de dicionários contendo os dados a serem exportados.
            caminho_arquivo (str): Caminho completo onde o arquivo Excel será salvo.

        Side effects:
            - Cria diretórios intermediários, se não existirem.
            - Salva o arquivo Excel no caminho especificado.
            - Imprime no console a confirmação do caminho onde o relatório foi gerado.
        """
        df = pd.DataFrame(dados)
        os.makedirs(os.path.dirname(caminho_arquivo), exist_ok=True)
        df.to_excel(caminho_arquivo, index=False)
        print(f"Relatório gerado: {caminho_arquivo}")

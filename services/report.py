import pandas as pd
import os

class ReportService:
    def gerar_excel(self, dados, caminho_arquivo):
        df = pd.DataFrame(dados)
        os.makedirs(os.path.dirname(caminho_arquivo), exist_ok=True)
        df.to_excel(caminho_arquivo, index=False)
        print(f"Relatório gerado: {caminho_arquivo}")

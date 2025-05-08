from services.api import APIService
from services.report import ReportService
from services.email import EmailService
from utils.helpers import calcular_media_caracteres

class Automacao:
    def __init__(self):
        self.api_service = APIService()
        self.report_service = ReportService()
        self.email_service = EmailService()

    def executar(self):
        usuarios = self.api_service.obter_usuarios()
        relatorio = []

        for usuario in usuarios:
            posts = self.api_service.obter_posts_por_usuario(usuario['id'])
            media = calcular_media_caracteres(posts)
            relatorio.append({
                'ID do Usuário': usuario['id'],
                'Nome do Usuário': usuario['name'],
                'Quantidade de Posts': len(posts),
                'Média de Caracteres dos Posts': media
            })

        caminho = 'output/relatorio.xlsx'
        self.report_service.gerar_excel(relatorio, caminho)
        self.email_service.simular_envio(caminho)

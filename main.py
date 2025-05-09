from services.automacao import Automacao

def main():
    """
    Função principal que inicia o processo de automação.

    A função:
    - Exibe uma mensagem de início.
    - Cria uma instância da classe Automacao.
    - Executa o método `executar()` que realiza a coleta, análise e geração de relatório.
    """
    print("Iniciando...")
    automacao = Automacao()
    automacao.executar()

if __name__ == '__main__':
    main()

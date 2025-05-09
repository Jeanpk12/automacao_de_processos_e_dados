# PROJETO_AUTOMACAO

## Descrição do Projeto

Este projeto automatiza o processo de coleta de dados de usuários e seus posts de uma API externa, realiza o cálculo de métricas sobre esses dados, gera um relatório consolidado em formato Excel e simula o envio deste relatório por e-mail.

O projeto serve para exemplificar um fluxo de automação que envolve:
* Integração com APIs externas (JSONPlaceholder para dados de usuários e posts).
* Processamento e análise de dados.
* Geração de relatórios.
* Simulação de notificações (envio de e-mail).

Ele resolve o problema de consolidar e analisar informações de usuários e suas postagens de forma automática, apresentando um resumo útil em um relatório.

## Tecnologias Utilizadas

* **Python 3.x**
* **Flask**: Para simular um endpoint de servidor de e-mail. 
* **Requests**: Para realizar chamadas HTTP à API externa e ao servidor de e-mail simulado.
* **Pandas**: Para manipulação de dados e geração do relatório em Excel. 
* **Openpyxl**: (Dependência do Pandas) Para escrita de arquivos Excel.
* **Unittest**: Para a suíte de testes automatizados.

## Instruções de Instalação

1.  **Clone o repositório (se aplicável):**
    ```bash
    git clone https://github.com/Jeanpk12/automacao_de_processos_e_dados.git
    cd automacao_de_processos_e_dados
    ```

2.  **Crie um ambiente virtual:**
    É recomendado utilizar um ambiente virtual para isolar as dependências do projeto.
    ```bash
    python -m venv venv
    ```

3.  **Ative o ambiente virtual:**
    * No Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    * No macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4.  **Instale as dependências:**
    O projeto utiliza um arquivo `requirements.txt` para listar suas dependências.
    ```bash
    pip install -r requirements.txt
    ```
    O conteúdo do `requirements.txt` deve ser:
    ```
    requests
    pandas
    openpyxl
    flask
    ```

## Como Rodar o Projeto

1.  **Inicie o servidor de simulação de e-mail (opcional, mas necessário para a funcionalidade completa):**
    O servidor `server.py` simula o recebimento de e-mails. Abra um terminal, navegue até a raiz do projeto e execute:
    ```bash
    python server.py
    ```
    Este servidor irá rodar na porta 5000 por padrão.

2.  **Execute o script principal de automação:**
    O script `main.py` é o ponto de entrada para iniciar o processo de automação. Abra outro terminal (com o ambiente virtual ativado), navegue até a raiz do projeto e execute:
    ```bash
    python main.py
    ```
    O script exibirá "Iniciando...", processará os dados, gerará o relatório e simulará o envio do e-mail.

## Como Executar os Testes

O projeto utiliza o módulo `unittest` do Python para testes. Os testes estão localizados na pasta `tests/`.

Para executar todos os testes, navegue até a raiz do projeto no terminal (com o ambiente virtual ativado) e utilize o comando de descoberta de testes do unittest:
```bash
python -m unittest discover tests
```
Alternativamente, você pode executar arquivos de teste individualmente:

```bash
python -m unittest tests.test_api_mock
python -m unittest tests.test_helpers
```
## Exemplos de Uso
Inputs:
- O script main.py não requer inputs diretos via linha de comando para sua execução principal.
- Ele consome dados da API pública https://jsonplaceholder.typicode.com (usuários e posts).   

Outputs Esperados:

1. Console Output durante a execução do ```main.py```:

- Mensagem de início: ```"Iniciando..."```   
- Confirmação da geração do relatório: ```"Relatório gerado: output/relatorio.xlsx"```   
- Confirmação da simulação de envio de e-mail (resposta do ```server.py```): ```"Resposta da API fictícia: {'status': 'sucesso', 'mensagem': 'E-mail enviado com sucesso (simulado)'}"```   
2. Arquivo de Relatório:

- Um arquivo Excel chamado ```relatorio.xlsx``` será criado na pasta ```output/```.
- Este relatório conterá as colunas: **'ID do Usuário'**, **'Nome do Usuário'**, **'Quantidade de Posts'**, **'Média de Caracteres dos Posts'**.   
3. Console Output durante a execução do ```server.py``` (se o ```main.py``` for executado):

Mensagem indicando o recebimento da simulação de e-mail: ```"Simulando envio de e-mail com os dados:"``` seguido dos dados do payload JSON.

## Estrutura de Diretórios
```yaml
PROJETO_AUTOMACAO/
├── main.py                 # Script principal que orquestra a automação
├── docs
    ├── api.md              # Documenta o modulo responsável por realizar a integração com a API JSONPlaceholder
    ├── automacao.md        # Documenta o modulo que centraliza e orquestra todo o processo de automação do sistema
    ├── overview.md         # Da uma visão geral do projeto
    ├── report.md           # Documenta a geração de relatório no formato Excel
├── server.py               # Servidor Flask para simular envio de e-mail
├── requirements.txt        # Lista de dependências do projeto
├── README.md               # Documentação do projeto (este arquivo)
├── output/                 # Diretório para arquivos gerados
│   └── relatorio.xlsx      # Relatório em Excel gerado pela automação
├── services/               # Módulos de serviço da aplicação
│   ├── api.py              # Serviço para interagir com a API JSONPlaceholder
│   ├── automacao.py        # Classe principal que orquestra o processo
│   ├── email.py            # Serviço para simular o envio de e-mails
│   └── report.py           # Serviço para gerar relatórios
├── tests/                  # Contém os testes automatizados
│   ├── test_api_mock.py    # Testes para o serviço de API com mock
│   └── test_helpers.py     # Testes para as funções utilitárias
└── utils/                  # Módulos com funções utilitárias
    └── helpers.py          # Funções auxiliares (ex: calcular_media_caracteres)
```

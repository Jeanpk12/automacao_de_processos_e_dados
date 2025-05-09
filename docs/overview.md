# Projeto: Relatório de Média de Caracteres
## Visão Geral
Este projeto automatiza o processo de coleta, análise e envio de relatórios sobre postagens de usuários. Ele consome dados de uma API, calcula estatísticas textuais (como a média de caracteres por post) e gera um relatório em Excel. Por fim, simula o envio desse relatório por e-mail para fins de validação.

Ideal para fins educacionais, testes ou protótipos onde se deseja entender pipeline de dados + geração de relatórios + integração com APIs.

## Estrutura do Projeto
```yaml
PROJETO_AUTOMACAO/
├── main.py
├── server.py ← servidor Flask com o endpoint /send-email
├── requirements.txt
├── services/
│   ├── api.py
│   ├── automacao.py
│   ├── email.py
│   └── report.py
├── utils/
│   └── helpers.py
└── tests/
    ├── test_api_mock.py
    └── test_helpers.py
```
## Como Funciona
1. **main.py:** inicia tudo, chamando a classe Automacao.

2. **Automacao:**
- Busca os usuários da API.
- Para cada um, pega os posts e calcula a média de caracteres.
- Gera uma planilha Excel com os resultados.
- Simula o envio do relatório via requisição POST para uma API Flask local.

3. **server.py:** apenas imprime os dados como se fosse um servidor de envio real.

## Teste Local
Execute a API Flask:
```bash
python server.py
```
Rode o processo principal:

```bash
python main.py
```

## Tecnologias Usadas
- **Python 3.x**
- **pandas** – manipulação e exportação de dados
- **Flask** – simulação de servidor de envio
- **requests** – requisições HTTP
- **openpyxl** – geração do relatório em Excel

## Resultados
Ao final do processo, será gerado:
- Um arquivo output/relatorio.xlsx
- ma simulação de envio de email

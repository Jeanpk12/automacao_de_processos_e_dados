# Automacao
Este módulo centraliza e orquestra todo o processo de automação do sistema, integrando os serviços de API, relatório e e-mail. A automação busca dados de usuários e seus posts, calcula métricas, gera um relatório em Excel e simula o envio por e-mail.

## Visão Geral
A classe Automacao realiza os seguintes passos:

1. Obtém todos os usuários da API.

2. Para cada usuário:

- Recupera os posts associados ao usuário.

- Calcula a média de caracteres dos posts.

- Agrega os dados para geração do relatório.

3. Gera um arquivo Excel com os dados agregados.

4. Simula o envio do relatório por e-mail.

## Estrutura Interna
## __init__()
Inicializa os serviços de:
- API (APIService)
- Relatório (ReportService)
- E-mail (EmailService)

## **executar()**
Executa a automação completa descrita acima.

## Fluxo da Automação
```css
[Início]
   ↓
[Obter usuários da API]
   ↓
[Para cada usuário]
   ↓
[→ Obter posts do usuário]
[→ Calcular média de caracteres dos posts]
[→ Adicionar dados ao relatório]
   ↓
[Gerar Excel com os dados]
   ↓
[Simular envio por e-mail]
   ↓
[Fim]
```

## Saída
output/relatorio.xlsx: Arquivo contendo:

- ID do Usuário

- Nome do Usuário

- Quantidade de Posts

- Média de Caracteres dos Posts

# Geração de Relatório em Excel
Este módulo é responsável por gerar um arquivo .xlsx com os dados coletados e processados durante a automação. O relatório é criado com base na biblioteca openpyxl, estruturado com colunas claras e dados agregados por usuário.

## Saída
- Arquivo gerado: ```output/relatorio.xlsx```

- Formato: Excel (.xlsx)

- Biblioteca usada: ```openpyxl```

- Criado por: ```ReportService.gerar_excel(dados: list[dict], caminho: str)```

Estrutura do Relatório
O arquivo Excel contém uma única planilha, com as seguintes colunas:

|Coluna	|Descrição|
|--------|----------|
|ID do Usuário	|ID único do usuário recuperado via API|
|Nome do Usuário	|Nome do usuário|
|Quantidade de Posts	|Número total de posts publicados por esse usuário|
|Média de Caracteres dos Posts	|Média de caracteres por post (usando calcular_media_caracteres)|

## Exemplo de Linha do Relatório
|id| nome|qtdPosts|media_de_caracteres|
|--|-----|--------|--------------------|
| 1 | Leanne Graham | 10 | 215.6 |


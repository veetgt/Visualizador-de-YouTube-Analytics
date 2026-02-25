# Análise de Dados do YouTube Analytics com Python

Esse é um projeto de análise de dados extraídos do YouTube Studio. Baseado em um artigo do freeCodeCamp.

## Tecnologias e Bibliotecas Utilizadas

* **Python:** Linguagem principal para a lógica de análise.
* **Pandas:** Carregamento de dados (`pd.read_csv`), limpeza, criação de novas métricas e manipulação de DataFrames.
* **Matplotlib & Seaborn:** Criação de visualizações estatísticas avançadas de forma simplificada e direta.

## Como Executar o Projeto

1. Faça o download dos seus dados no YouTube Studio acessando o "Modo Avançado" e clicando em "Exportar CSV".
2. Na pasta exportada, localize o arquivo principal chamado `Table data.csv` ou `Dados da tabela.csv`.
3. Abra este arquivo e remova a primeira linha (que contém os totais gerais do canal) para evitar distorções nos cálculos.
4. Coloque o arquivo limpo na mesma pasta do seu script ou notebook Python.
5. Execute os programas para gerar os gráficos e visualizar os insights.

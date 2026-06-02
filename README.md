
Mini Projeto de Análise de Dados - Varejo

Descrição

Este projeto tem por objetivo realizar uma análise exploratória de dados de um conjunto de vendas do varejo, utilizando Python e a biblioteca Pandas e NumPy.
A análise busca entender o comportamento dos clientes e gerar insights a partir dos dados.

OBJETIVOS:
Explorar e limpar a base de dados; Identificar padrões de clientes e produtos; Aplicar Estatística Descritiva; Gerar insights para apoio à tomada de decisão.

TECNOLOGIA UTILIZADA:
Python; Pandas; NumPy; Visual Studio Code; GitHub; Matplotlib

ETAPAS DO PROJETO:
1. IMPORTAÇÃO DOS DADOS (Carregamento da base de dados utilizando Pandas);
2. LIMPEZA E TRATAMENTO (Remoção de Duplicatas,tratamento de valores nulos.criação da base tratada (df_limpo)
3. ANÁLISE EXPLORATÓRIA
4. ESTATÍSTICA DESCRITIVA
5. RELATÓRIO E DOCUMENTAÇÃO

 ANÁLISE REALIZADA:
- Leitura da base de dados
- Limpeza de dados (remoção de duplicatas e colunas inúteis)
- Tratamento de valores ausentes e inconsistentes
- Conversão de datas
- Análise estatística descritiva (média, mediana, moda, desvio padrão
- Agrupamentos por categorias (gênero, estado civil, produtos e categorias)
- Identificação de produtos mais vendidos
- Análise de categorias de vendas/análise da variável CL_FHL (número de filhos)
  
  
BASE DE DADOS:

A base utilizada contém informações como:
Data da compra; ID do cliente; Gênero; Estado Civil; Número de filhos (CL_FHL);
Segmento; Categoria do produto; Nome do produto.

ESTRUTURA DO PROJETO:

Mini Projeto Varejo/
├── Dados/
│ └── Base Varejo.csv
├── scripts/
│ ├── varejo.py
│ └── main.py
└── README.md


COMO EXECUTAR O PROJETO:

1. Abra o projeto no VS Code
2. Instale as bibliotecas necessárias (se precisar):
   ```bash
   pip install pandas matplotlib
3.	Execute o arquivo principal: 
python scripts/varejo.py (principal)
ou
python scripts/main.py

PRINCIPAIS INSIGHTS:

A maioria dos clientes possuem pouco ou nenhum filho;
A distribuição da variável apresenta assimetria;
Ha variação moderada no número de filhos entre os clientes.

VERSIONAMENTO:

O projeto foi versionado utilizanto GitHub,com envio dos principais arquivos para o repositório da turma:
Script de análise (.py);
README.md;
Base de dados tratada (df_limpo)

CONCLUSÃO:

Este projeto permitiu aplicar conceitos fundamentais de análise de dados, desde a limpeza até interpretação estatística de uma base real.


AUTOR:
Projeto desenvolvido por LUCIANA SANTOS DE AZEVEDO, TURMA T2, durante o curso de Análise de Dados do Senai ( SCTEC).

OBSERVAÇÃO:
Os dados foram tratados e analisados com foco em aprendizado de análise exploratória (EDA).



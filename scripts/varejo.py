import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('Dados/Base Varejo.csv', sep=';')
#LIMPEZA
df = df.drop_duplicates()
df['DATA'] = pd.to_datetime(df['DATA'],dayfirst=True, errors='coerce')
df['PR_CAT'] = df['PR_CAT'].replace('#N/D','Desconhecido')
df = df.drop(columns=[col for col in df.columns if "Unnamed" in col])
#Analise exploratoria
print('Base carregada!')
print(df.shape)
print('\ncolunas')
print(df.columns)
print('\ntipos')
print(df.dtypes)
print('\nNulos')
print(df.isnull().sum())
print('\nDuplicatas')
print(df.duplicated().sum())
print('\nAmostra')
print(df.head())
print('\n===============')
print('Diagnostico Qualidade')
print('===============')
print('nNulos por coluna')
print(df.isnull().sum())
duplicatas = df.duplicated().sum()
print('\ntotal duplicatas')
print(duplicatas)
print('\ncategorias vazias')
if "PR_CAT" in df.columns:
    categorias_vazias = (df['PR_CAT'].isnull().sum())
    print(categorias_vazias)
else:
    print("Coluna PR_CAT nao encontrada")
print('\nVERIFICANDO DATAS')
df['DATA'] = pd.to_datetime(df['DATA'],dayfirst=True, errors='coerce')
datas_invalidas = df['DATA'].isnull().sum()
print('\ntotal datas invalidas')
print(datas_invalidas)
df = df.drop_duplicates()
df['PR_CAT'] = df['PR_CAT'].replace('#N/D', 'Desconhecido')
print("\nNovo tamanho após remover duplicatas:")
print(df.shape)
print(df.columns)
print("\nESTATISTICA DESCRITIVA - FILHOS")
print("contagem:", df['CL_FHL'].count())
print("media:", df['CL_FHL'].mean())
print("mediana:", df['CL_FHL'].median())
print("Moda:", df['CL_FHL'].mode()[0])
print("desvio padrao:", df['CL_FHL'].std())
print("minimo:", df['CL_FHL'].min())
print("maximo:", df['CL_FHL'].max())
print("\nQuartis:")
print(df['CL_FHL'].describe())
#df["CL_FHL"].hist(bins=10)
#plt.title("distribuição do numero de filhos(CL_FHL)")
#plt.xlabel("numero de filhos")
#plt.ylabel("frequencia")
#plt.show()
print("\n=== Quantidade de clientes por genero ===")
print(df['CL_GENERO'].value_counts())
#Estatistica Descritiva
print(df['CL_FHL'].describe())
print(df['CL_GENERO'].value_counts())
print("\n=== COLUNAS DA BASE ===")
print(df.columns.tolist())
df = df.drop(columns=[col for col in df.columns if "Unnamed" in col])
print("\n=== Clientes por genero ===")
#Agrupamento
print(df.groupby("CL_GENERO")["CL_ID"].nunique())
print("\n=== Media de filhos por genero ===")
print(df.groupby("CL_GENERO")["CL_FHL"].mean())
print("\n=== Clientes por estado civil ===")
print(df.groupby("CL_EC")["CL_ID"].nunique())
print("\n=== Produtos mais vendidos ===")
print(df["PR_NOME"].value_counts().head(10))
print("\n=== Categorias mais vendidas ===")
print(df["PR_CAT"].value_counts())
print("\n=== vendas por categoria ===")
print(df.groupby("PR_CAT")["CO_ID"].count())


 

















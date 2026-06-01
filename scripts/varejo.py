import pandas as pd
df = pd.read_csv('Dados/Base Varejo.csv', sep=';')
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
print("\nNovo tamanho após remover duplicatas:")
print(df.shape)
print(df.columns)
print("\nESTATISTICA DESCRITIVA - FILHOS")
print("contagem:", df['CL_FHL'].count())
print("media:", df['CL_FHL'].mean())
print("mediana:", df['CL_FHL'].median())
print("Moda:", df['CL_FHL'].mode())
print("desvio padrao:", df['CL_FHL'].std())
print("minimo:", df['CL_FHL'].min())
print("maximo:", df['CL_FHL'].max())
print("\nQuartis:")
print(df['CL_FHL'].describe())
import matplotlib.pyplot as plt
#df["CL_FHL"].hist(bins=10)
#plt.title("distribuição do numero de filhos(CL_FHL)")
#plt.xlabel("numero de filhos")
#plt.ylabel("frequencia")
#plt.show()
import matplotlib.pyplot as plt
#plt.show()
df.columns
print("\n=== Quantidade de clientes por genero ===")
print(df['CL_GENERO'].value_counts())
print('cheguei aqui')
print(df['CL_FHL'].describe())
print('vou contar generos')
print(df['CL_GENERO'].value_counts())














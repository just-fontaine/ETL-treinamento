# %%
import pandas as pd
import pyodbc

# %%

server = r'DESKTOP-5KQL2U6\MSSQLSERVER01'
database = 'Python'
conexaoDB = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                           f'SERVER={server};'
                           f'DATABASE={database};'
                           'Trusted_Connection=yes;')

cursor = conexaoDB.cursor()

# %%
df = pd.read_excel(r'C:\fora do onedrive\Python Scripts\SQL\fazendo minhas coisas\banco de dados mercado\banco de dados mercado.xlsx')

# %%
cursor.execute('truncate table [Mercado]') #exclui o original para não sobrepor

# %%
for index, linha in df.iterrows():
    cursor.execute('''INSERT INTO [Mercado] (Produtos, Categoria, Preco, ID, Marca, Estoque,
                   Validade, Fornecedor, Preco_Por_Unidade, Origem, Peso) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                   linha.Produtos, linha.Categoria, linha.Preco, linha.ID,
                   linha.Marca, linha.Estoque, linha.Validade,
                   linha.Fornecedor, linha.Preco_Por_Unidade, linha.Origem,
                   linha.Peso)


cursor.commit()
cursor.close()
conexaoDB.close()

# %%
'''

CREATE TABLE Mercado(
    [Produtos] nvarchar(255),
	[Categoria] nvarchar(255),
	[Preco] float,
	[ID] int,
	[Marca] nvarchar(255),
	[Estoque] int,
	[Fornecedor] nvarchar(255),
	[Preco_Por_Unidade] nvarchar(255),
	[Origem] nvarchar(255),
	[Peso] nvarchar(255),
	[Validade] date
);

'''

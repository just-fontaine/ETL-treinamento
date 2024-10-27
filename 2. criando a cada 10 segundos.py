# %%
def job():
    import pandas as pd
    import subprocess
    import sys

    try:
        import pyodbc
    except ImportError:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyodbc'])

    server = r'DESKTOP-5KQL2U6\MSSQLSERVER01'
    database = 'Python'
    conexaoDB = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                            f'SERVER={server};'
                            f'DATABASE={database};'
                            'Trusted_Connection=yes;')

    cursor = conexaoDB.cursor()

    df = pd.read_excel(r'C:\fora do onedrive\Python Scripts\SQL\fazendo minhas coisas\banco de dados mercado\banco de dados mercado.xlsx')
    cursor.execute('truncate table [Mercado]')

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


import schedule
import time

schedule.every(10).seconds.do(job)  

try:
    while True:
        schedule.run_pending()
        time.sleep(1)
except KeyboardInterrupt:
    print('alguem apertou pra parar.')

import cx_Oracle
import pandas as pd
import time

dsn_tns = cx_Oracle.makedsn("ORACLE.FIAP.COM.BR", 1521, service_name="ORCL")
conn = cx_Oracle.connect(user="RM560401", password="180206", dsn=dsn_tns)
cursor = conn.cursor()

def popularPaises():
    csv_file = "CsvPaises.csv" 
    
    try:
        df = pd.read_csv(csv_file, sep=",") 
        print("Arquivo CSV carregado com sucesso!")


        for index, row in df.iterrows():
            cursor.execute("""
                INSERT INTO Paises (id_pais, nome, continente)
                VALUES (:1, :2, :3)
            """, (row['id'], row['nome'], row['continente']))
        
        
        conn.commit()
        print("Dados inseridos com sucesso na tabela 'Paises'!")

    except pd.errors.EmptyDataError:
        print("Erro ao carregar o CSV: O arquivo está vazio ou corrompido.")
    except cx_Oracle.DatabaseError as e:
        print("Erro ao inserir dados no banco de dados:", e)

    cursor.close()
    conn.close()

def popularRegioes():
    csv_file = "CsvRegioes.csv" 
    
    try:
        df = pd.read_csv(csv_file, sep=",") 
        print("Arquivo CSV carregado com sucesso!")


        for index, row in df.iterrows():
            cursor.execute("""
                INSERT INTO Regiao(id_regiao, pais_id, nome)
                VALUES (:1, :2, :3)
            """, (row['id'], row['pais_id'], row['nome']))
        
        
        conn.commit()
        print("Dados inseridos com sucesso na tabela 'Regiao'!")

    except pd.errors.EmptyDataError:
        print("Erro ao carregar o CSV: O arquivo está vazio ou corrompido.")
    except cx_Oracle.DatabaseError as e:
        print("Erro ao inserir dados no banco de dados:", e)

    cursor.close()
    conn.close()

def popularAno():
    csv_file = "CsvAno.csv" 

    try:
        df = pd.read_csv(csv_file, sep=",") 
        print("Arquivo CSV carregado com sucesso!")


        for index, row in df.iterrows():
            
            cursor.execute("""
                INSERT INTO Ano (id_ano, ano)
                VALUES (:1, :2)
            """, (int(row['id_ano']), int(row['ano'])))
        
        conn.commit()
        print("Dados inseridos com sucesso na tabela 'Ano'!")

    except pd.errors.EmptyDataError:
        print("Erro ao carregar o CSV: O arquivo está vazio ou corrompido.")
    except cx_Oracle.DatabaseError as e:
        print("Erro ao inserir dados no banco de dados:", e)

    cursor.close()
    conn.close()

def popularPaisAno():
    csv_file = "CsvPaisAno.csv" 

    try:
        df = pd.read_csv(csv_file, sep=",") 
        print("Arquivo CSV carregado com sucesso!")

        for index, row in df.iterrows():
            
            cursor.execute("""
                INSERT INTO Pais_Ano (id_pais_ano, ano_id, pais_id, media_per_capita, media_tarifa)
                VALUES (:1, :2,:3,:4,:5)
            """, (row['id'], int(row['ano_id']),int(row['pais_id']),float(row['media_per_capita']),float(row['media_tarifa'])))
        

        conn.commit()
        print("Dados inseridos com sucesso na tabela 'Pais_Ano'!")

    except pd.errors.EmptyDataError:
        print("Erro ao carregar o CSV: O arquivo está vazio ou corrompido.")
    except cx_Oracle.DatabaseError as e:
        print("Erro ao inserir dados no banco de dados:", e)

    cursor.close()
    conn.close()

def popularConsumoTarifas():
    csv_file = "CsvConsumoTarifa.csv" 

    try:
        df = pd.read_csv(csv_file, sep=",") 
        print("Arquivo CSV carregado com sucesso!")
       
        for index, row in df.iterrows():
            
            cursor.execute("""
                INSERT INTO Consumo_Tarifas(id_consumo_tarifas, regiao_id, ano_id,consumo_total,consumo_per_capita,consumidores,tarifa)
                VALUES (:1, :2, :3, :4, :5, :6, :7)
            """, (int(row['id_consumo_tarifas']), int(row['regiao_id']), int(row['ano_id']), float(row['consumo_total']), float(row['consumo_per_capita']), float(row['consumidores']), float(row['tarifa'])))
        
        conn.commit()
        print("Dados inseridos com sucesso na tabela 'Consumo_Tarifas'!")

    except pd.errors.EmptyDataError:
        print("Erro ao carregar o CSV: O arquivo está vazio ou corrompido.")
    except cx_Oracle.DatabaseError as e:
        print("Erro ao inserir dados no banco de dados:", e)

    cursor.close()
    conn.close()

#Rode o arquivo chamando cada funcao por vez

#popularPaises()
#popularRegioes()
#popularAno()
#popularPaisAno()
popularConsumoTarifas()


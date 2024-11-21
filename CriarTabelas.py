import cx_Oracle

dsn_tns = cx_Oracle.makedsn("ORACLE.FIAP.COM.BR", 1521, service_name="ORCL")
conn = cx_Oracle.connect(user="RM560401", password="180206", dsn=dsn_tns)
cursor = conn.cursor()

try:
    cursor.execute("""
        CREATE TABLE Paises (
            id_pais INT PRIMARY KEY,
            nome VARCHAR2(100) NOT NULL,
            continente VARCHAR2(50) NOT NULL
        )
    """)
    print("Tabela 'Paises' criada com sucesso.")

    cursor.execute("""
        CREATE TABLE Regiao (
            id_regiao INT PRIMARY KEY,
            pais_id INT NOT NULL,
            nome VARCHAR2(100) NOT NULL,
            FOREIGN KEY (pais_id) REFERENCES Paises(id_pais)
        )
    """)
    print("Tabela 'Regiao' criada com sucesso.")

    cursor.execute("""
        CREATE TABLE Ano (
            id_ano INT PRIMARY KEY,
            ano INT NOT NULL
        )
    """)
    print("Tabela 'Ano' criada com sucesso.")

    cursor.execute("""
        CREATE TABLE Consumo_Tarifas (
            id_consumo_tarifas INT PRIMARY KEY,
            regiao_id INT NOT NULL,
            ano_id INT NOT NULL,
            consumo_total FLOAT NOT NULL,
            consumo_per_capita FLOAT,
            consumidores  NUMBER(11),
            tarifa FLOAT,
            FOREIGN KEY (regiao_id) REFERENCES Regiao(id_regiao),
            FOREIGN KEY (ano_id) REFERENCES Ano(id_ano)
        )
    """)
    print("Tabela 'Consumo_Tarifas' criada com sucesso.")

    cursor.execute("""
        CREATE TABLE Pais_Ano (
            id_pais_ano INT PRIMARY KEY,
            ano_id INT NOT NULL,
            pais_id INT NOT NULL,
            media_per_capita FLOAT,
            media_tarifa FLOAT,
            FOREIGN KEY (pais_id) REFERENCES Paises(id_pais),
            FOREIGN KEY (ano_id) REFERENCES Ano(id_ano)
        )
    """)
    print("Tabela 'Pais_Ano' criada com sucesso.")

except cx_Oracle.DatabaseError as e:
    print("Erro ao criar as tabelas:", e)

cursor.close()
conn.close()

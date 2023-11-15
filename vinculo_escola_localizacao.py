# esse programa cria tabela tp_localizacao e escola_localizacao

'''
Esse programa é referente à questão 3
Esse programa irá criar as tabelas de vinculação, bem como as tabelas
com as informações necessárias para realizar as pesquisas conforme
as informações vinculadas
'''

import csv
import sqlite3

con = sqlite3.connect('dsbd.db')
cur = con.cursor()

cur.execute("DROP TABLE IF EXISTS tp_localizacao")
cur.execute("DROP TABLE IF EXISTS escola_localizacao")
cur.execute("DROP TABLE IF EXISTS tp_dependencia")
cur.execute("DROP TABLE IF EXISTS tp_situacao")
cur.execute("DROP TABLE IF EXISTS escola_dependencia")
cur.execute("DROP TABLE IF EXISTS escola_situacao")
# CRIAR TABELAS DOS VINCULOS
cur.execute("""CREATE TABLE tp_localizacao(
                codigo INT PRIMARY KEY,
                nome TEXT NOT NULL UNIQUE,
                descricao TEXT NOT NULL UNIQUE)
            """)
cur.execute("""CREATE TABLE tp_dependencia(
                codigo INT PRIMARY KEY,
                nome TEXT NOT NULL UNIQUE)
            """)
cur.execute("""CREATE TABLE tp_situacao(
                codigo INT PRIMARY KEY,
                nome TEXT NOT NULL UNIQUE)
            """)
# POPULAR AS TABELAS DE VINCULO
cur.execute("""INSERT INTO tp_localizacao VALUES 
                (1, 'Urbana', 'Escola encontra-se em região urbana'),
                (2, 'Rural', 'Escola encontra-se em região rural')
            """)
cur.execute("""INSERT INTO tp_dependencia VALUES 
                (1, 'Federal'),
                (2, 'Estadual'),
                (3, 'Municipal'),
                (4, 'Privada')
            """)
cur.execute("""INSERT INTO tp_situacao VALUES 
                (1, 'Em atividade'),
                (2, 'Paralisada'),
                (3, 'Extinta(ano censo)'),
                (4, 'Extinta em anos anteriores')
            """)
# CONTEUDO VINCULADO
cur.execute("""CREATE TABLE escola_localizacao(
                escola_codigo  INT NOT NULL,
                localizacao_codigo INT NOT NULL,
                PRIMARY KEY (escola_codigo,localizacao_codigo),
                FOREIGN KEY (escola_codigo) REFERENCES escola(codigo),
                FOREIGN KEY (localizacao_codigo) REFERENCES tp_localizacao(codigo))
            """)
cur.execute("""CREATE TABLE escola_dependencia(
                escola_codigo  INT NOT NULL,
                dependencia_codigo INT NOT NULL,
                PRIMARY KEY (escola_codigo,dependencia_codigo),
                FOREIGN KEY (escola_codigo) REFERENCES escola(codigo),
                FOREIGN KEY (dependencia_codigo) REFERENCES tp_dependencia(codigo))
            """)
cur.execute("""CREATE TABLE escola_situacao(
                escola_codigo  INT NOT NULL,
                situacao_codigo INT NOT NULL,
                PRIMARY KEY (escola_codigo,situacao_codigo),
                FOREIGN KEY (escola_codigo) REFERENCES escola(codigo),
                FOREIGN KEY (situacao_codigo) REFERENCES tp_situacao(codigo))
            """)
con.commit()
"""
Esse programa é referente à questão 4
irá adicionar 5 medições à uma nova tabela, também criada por esse código, chamada censo: 
quantidade de alunos do ensino médio,se a escola dispõe de água potável, possui acesso à internet,
disponibiliza desktop para os alunos, realiza separação do lixo, 
"""

import csv
import sqlite3

con = sqlite3.connect('dsbd.db') #conexão com o banco de dados do exercício
cur = con.cursor() #cursor para executar comandos

cur.execute("DROP TABLE IF EXISTS censo")

cur.execute("""CREATE TABLE censo(
                ano_censo NOT NULL,
                escola_codigo NOT NULL UNIQUE,
                alunos_medio NOT NULL,
                acesso_internet NOT NULL,
                desktop_aluno NOT NULL,
                lixo_separacao NOT NULL,
                agua_potavel NOT NULL,
                PRIMARY KEY (ano_censo, escola_codigo))
            """)
medicoes_censo = [] #variável para armazenar o conteúdo que será inserido no bd

with open('microdados_1k.csv', encoding = " ISO-8859-1") as dados_csv: #abrir o csv que contém infos
    leitor = csv.DictReader(dados_csv, delimiter=';') #variável para ler o csv
    for linha in leitor: #interação que escreve na variável conteudo_escola
        medicoes_censo.append((linha["NU_ANO_CENSO"],
                                linha["CO_ENTIDADE"],
                                linha["QT_MAT_MED"],
                                linha["IN_INTERNET"],
                                linha["IN_DESKTOP_ALUNO"],
                                linha["IN_TRATAMENTO_LIXO_SEPARACAO"],
                                linha["IN_AGUA_POTAVEL"])
                                )

cur.executemany("INSERT INTO censo VALUES(?, ?, ?,?,?,?,?)", medicoes_censo)
con.commit() #commit para validar execute
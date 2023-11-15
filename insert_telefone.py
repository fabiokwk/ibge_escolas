'''
Esse programa é referente à questão 2
Escreve o conteúdo da tabela telefone:
código da escola
ddd
número telefônico
'''

import csv
import sqlite3

con = sqlite3.connect('dsbd.db') #conexão com o banco de dados do exercício
cur = con.cursor() #cursor para executar comandos

conteudo_telefone = [] #variável para armazenar o conteúdo que será inserido no bd

with open('microdados_1k.csv', encoding = " ISO-8859-1") as dados_csv: #abrir o csv que contém infos
    leitor = csv.DictReader(dados_csv, delimiter=';') #variável para ler o csv
    for linha in leitor: #interação que escreve na variável conteudo_telefone
        conteudo_telefone.append((linha["CO_ENTIDADE"],
                                linha["NU_DDD"], 
                                linha["NU_TELEFONE"])) 

print(conteudo_telefone[0:6])
cur.executemany("INSERT INTO telefone (cod_escola, ddd, numero) VALUES(?, ?, ?)", conteudo_telefone)
con.commit() #commit para validar execute
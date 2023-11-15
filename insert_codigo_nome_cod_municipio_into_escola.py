'''
Esse programa é referente à questão 1
Escreve na tabela escola as informações:
código
nome
código do município
'''

import csv
import sqlite3

con = sqlite3.connect('dsbd.db') #conexão com o banco de dados do exercício
cur = con.cursor() #cursor para executar comandos

conteudo_escola = [] #variável para armazenar o conteúdo que será inserido no bd

with open('microdados_1k.csv', encoding = " ISO-8859-1") as dados_csv: #abrir o csv que contém infos
    leitor = csv.DictReader(dados_csv, delimiter=';') #variável para ler o csv
    for linha in leitor: #interação que escreve na variável conteudo_escola
        conteudo_escola.append((linha["CO_ENTIDADE"],
                                linha["NO_ENTIDADE"], 
                                linha["CO_MUNICIPIO"])) 

print(conteudo_escola[0:6])
cur.executemany("INSERT INTO escola (codigo, nome, cod_municipio) VALUES(?, ?, ?)", conteudo_escola)
con.commit() #commit para validar execute
''' 
Esse programa mostra o resultado das 3 vinculações escolhidas
nome da escola com a localização
nome da escola com a dependencia
nome da escola com a situação

'''
import csv
import sqlite3

con = sqlite3.connect('dsbd.db')
cur = con.cursor()

cur.execute("""SELECT escola.nome, tp_localizacao.nome FROM escola
                 INNER JOIN escola_localizacao ON escola.codigo = escola_localizacao.escola_codigo
                 INNER JOIN tp_localizacao ON escola_localizacao.localizacao_codigo = tp_localizacao.codigo
            """)

result_localizacao = cur.fetchall()

cur.execute("""SELECT escola.nome, tp_dependencia.nome FROM escola
                 INNER JOIN escola_dependencia ON escola.codigo = escola_dependencia.escola_codigo
                 INNER JOIN tp_dependencia ON escola_dependencia.dependencia_codigo = tp_dependencia.codigo
            """)

result_dependencia = cur.fetchall()

cur.execute("""SELECT escola.nome, tp_situacao.nome FROM escola
                 INNER JOIN escola_situacao ON escola.codigo = escola_situacao.escola_codigo
                 INNER JOIN tp_situacao ON escola_situacao.situacao_codigo = tp_situacao.codigo
            """)

result_situacao = cur.fetchall()

print(result_localizacao[0:5])
print(len(result_localizacao))

print(result_dependencia[0:5])
print(len(result_dependencia))

print(result_situacao[0:5])
print(len(result_situacao))


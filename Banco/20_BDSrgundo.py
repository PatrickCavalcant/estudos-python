import sqlite3
conexao = sqlite3.connect("agenda.bd")
cursor = conexao.cursor()
cursor. execute('''select * from agenda''')
resultado = cursor.fetchall()
for registro in resultado:
    print("nome: %s\n telefone: %s" %(registro))
cursor.close()
conexao.close()

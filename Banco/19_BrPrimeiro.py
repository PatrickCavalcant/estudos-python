import sqlite3
conexao = sqlite3.connect("agenda.bd")
cursor = conexao.cursor()
cursor. execute('''
         create table agenda(
             nome text,
             telefone text)
         ''')
cursor.execute('''
        insert into agenda(nome, telefone)
        values(?, ?)
        ''',("nilo", "9999-0090"))
conexao.commit()
cursor.close()
conexao.close()
         


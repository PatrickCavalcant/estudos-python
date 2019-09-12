import sqlite3
dados=[("joao","0000-000"),
      ("andre", "92992-292"),
      ("maria","92992-010")]
conexao = sqlite3.connect("agenda.bd")
cursor = conexao.cursor()
cursor.executemany('''
        insert into agenda(nome, telefone)
        values(?, ?)
        ''', dados)
conexao.commit()
cursor.close()
conexao.close()

import sqlite3

DATABASE = 'user.db'

# Conectar ao banco de dados (ou criar se não existe)
conn = sqlite3.connect(DATABASE)

# Criar um cursor
cursor = conn.cursor()

# Criar uma tabela
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Usuarios (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        idade INTEGER
    )
''')

# Inserir dados
cursor.execute('INSERT INTO Usuarios (nome, idade)  VALUES (?, ?)', ('Bárbara', '21'))
cursor.execute('INSERT INTO Usuarios (nome, idade)  VALUES (?, ?)', ('Victor', '10'))

# Commit para salvar as alterações
conn.commit()

# Consultar dados
cursor.execute('SELECT * FROM Usuarios')
for row in cursor.fetchall():
    print(row)

# Fechar a conexão
conn.close()
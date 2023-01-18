import sqlite3

# criando banco
conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()

def criar_tabela():
    cursor.execute("""
    CREATE TABLE clientes (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER,
        cpf VARCHAR(11) NOT NULL
        );
    """)
    
#criar_tabela()

def add_cliente():
    cursor.execute("""
    INSERT INTO clientes (
        nome, idade, cpf
        )
    VALUES (
        'BOB', 42, 987654321
        );
    """)
    conn.commit()
    
#add_cliente()

def ler_dados():
    cursor.execute("""
    SELECT * FROM clientes (
    """)
    for cliente in cursor.fetchall():
        print(cliente)
    
#ler_dados()

def atualizar():
    id = 3
    novo_nome = 'Bob'
    nova_idade = 40
    novo_cpf = 987654320
    cursor.execute("""
    UPDATE clientes
    SET nome = ?, idade = ?, cpf = ? WHERE id = ?
    """, (novo_nome, nova_idade, novo_cpf, id)
    )
    conn.commit()
    
#atualizar()

def remover():
    cursor.execute("""
    DELETE FROM clientes WHERE nome = 'BOB'
    """)
    conn.commit()
    
#remover()
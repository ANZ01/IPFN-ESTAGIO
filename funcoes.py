import sqlite3

def insertCliente(nome,idade,telefone,morada,codpostal,email):
    conn = sqlite3.connect('vectrix.db')
    conn.execute("PRAGMA foreign_keys = ON")  # Enable foreign key support
    cursor = conn.cursor()
    cursor.execute(("INSERT INTO Cliente (Nome, Idade, Telefone, Morada, Cod_Postal, Email) Values(?,?,?,?,?,?)"), (nome,idade,telefone,morada,codpostal,email))
    conn.commit()
    conn.close

def Select():
    conn = sqlite3.connect('vectrix.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM CLIENTE")
    data = cursor.fetchall()
    print(data[0])
    conn.close

def insertPostal( codigo,localidade):
    conn = sqlite3.connect('vectrix.db')
    conn.execute("PRAGMA foreign_keys = ON")  # Enable foreign key support
    cursor = conn.cursor()
    cursor.execute(("INSERT INTO Postal(Codigo, Localidade) VALUES(?,?)"), (codigo,localidade))
    conn.commit()
    conn.close

def insertEmpregado(nome, salario, telefone, morada, codpostal, email):
    conn = sqlite3.connect('vectrix.db')
    conn.execute("PRAGMA foreign_keys = ON")  # Enable foreign key support
    cursor = conn.cursor()
    cursor.execute(("INSERT INTO Empregado(Nome,Salario,Telefone,Morada,Cod_Postal,Email) Values(?,?,?,?,?,?)"),(nome,salario,telefone,morada,codpostal,email))
    conn.commit()
    conn.close


def insertEncomenda(codcliente,codempregado,codprod,descricao):
    conn = sqlite3.connect('vectrix.db')
    conn.execute("PRAGMA foreign_keys = ON")  # Enable foreign key support
    cursor = conn.cursor()
    cursor.execute(("INSERT INTO Encomenda(Cod_Cliente, Cod_Empregado, Cod_Prod, Descricao) Values(?,?,?,?)"),(codcliente,codempregado,codprod,descricao))
    conn.commit()
    conn.close

def insertComissao(codcliente,codservico,valor):
    conn = sqlite3.connect('vectrix.db')
    conn.execute("PRAGMA foreign_keys = ON")  # Enable foreign key support
    cursor = conn.cursor()
    cursor.execute(("INSERT INTO Comissao( Cod_Cliente, Cod_Servico, Valor) Values(?,?,?)"), (codcliente,codservico,valor))
    conn.commit()
    conn.close

def insertProduto(codfornecedor, descricao):
    conn = sqlite3.connect('vectrix.db')
    conn.execute("PRAGMA foreign_keys = ON")  # Enable foreign key support
    cursor = conn.cursor()
    cursor.execute(("INSERT INTO Produto(Cod_Fornecedor,Descricao) Values(?,?)"), (codfornecedor,descricao))
    conn.commit()
    conn.close

def insertFornecedor(nome, morada, codpostal, telefone, email):
    conn = sqlite3.connect('vectrix.db')
    conn.execute("PRAGMA foreign_keys = ON")  # Enable foreign key support
    cursor = conn.cursor()
    cursor.execute(("INSERT INTO Fornecedor(Nome, Morada, Cod_Postal, Telefone, Email) Values(?,?,?,?,?)"), (nome, morada, codpostal, telefone, email))
    conn.commit()
    conn.close

def insertServico(descricao):
    conn = sqlite3.connect('vectrix.db')
    conn.execute("PRAGMA foreign_keys = ON")  # Enable foreign key support
    cursor = conn.cursor()
    cursor.execute(("INSERT INTO Servico(Descricao) VALUES (?)"), (descricao,))
    conn.commit()
    conn.close

Select()
import sqlite3
import csv

def importcsv(arq_csv):
    conn = sqlite3.connect('NuclearReactor.db') #CONEXAO COM A BASE DE DADOS
    cursor = conn.cursor() #CRIA UM CURSOR, PERMITE MANIPULAR DIRETAMENTE A BASE DE DADOS
    with open(arq_csv, 'r') as arquivo: #ABRE O ARQUIVO CSV DESEJADO

        leitor_csv = csv.reader(arquivo) #CARREGA OS DADOS DO ARQUIVO NA VARIAVEL LEITOR_CSV
        next(leitor_csv) #LE A PRIMEIRA LINHA EM LEITOR_CSV
        for linha in leitor_csv:
            nfp = linha[2]
            tipo = linha[3]

            if nfp.isdigit() and 1 <= int(nfp) <= 10 and tipo == "False": # FILTRA TODOS OS QA, STELLARATORS DE TIPO 1
                linha[3] = 1
                linha = [float(valor) for valor in linha]
                linha[3] = 1
                linha[2] = int(linha[2])
                cursor.execute(f"Insert Or Ignore Into Omnigenous(axLength, RotTrans, nfp, Tipo, rc1, zs1, etabar, max_elong, lgradB, min_RO) VALUES(?,?,?,?,?,?,?,?,?,?)", linha)
                print(f"valid insert")

            else:

                if nfp.isdigit() and 1 <= int(nfp) <= 10 and tipo == "True": #FILTRA OS QH, STELLARATORS DE TIPO 2
                    linha[3] = 2
                    linha = [float(valor) for valor in linha]
                    linha[3] = 2
                    linha[2] = int(linha[2])
                    cursor.execute(f"Insert Or Ignore Into Omnigenous(axLength, RotTrans, nfp, Tipo, rc1, zs1, etabar, max_elong, lgradB, min_RO) VALUES(?,?,?,?,?,?,?,?,?,?)", linha)
                    print(f"valid insert")
                else:

                     print(f"invalid insert")
    conn.commit() # FAZ COM QUE AS ALTERAÇOES QUE FIZ À BASE DE DADOS SEJAM REALIZADAS
    conn.close() #FECHA A CONEXÃO COM A BASE DE DADOS


def selectdata():
    conn = sqlite3.connect('NuclearReactor.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Omnigenous")
    data = cursor.fetchall() #PEGA NO ENDEREÇO ONDE FORAM GUARDADOS OS VALORES SELECIONADOS NA LINHA ANTERIOR (LINHA 42) E 'TRADUZ' OS VALORES PARA A NOSSA LINGUA
    for row in data:
        print(row)
        print("\n")
    conn.close()

def CreateTable():
    conn = sqlite3.connect('NuclearReactor.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE Omnigenous (axLength float check(axLength>0), RotTrans Float check(RotTrans>0),nfp INTEGER check ( nfp between 1 and 10),Tipo integer REFERENCES Tipo(Tipo),rc1 Float,zs1 Float,eta Float,max_elong float,lgradB Float check(lgradB>0),min_RO Float check ( min_RO>0))")
    conn.commit()
    conn.close()

importcsv('qsc_out.random_scan_nfp2_2ndorder.csv') #IMPORTCSV(ARQUIVO CSV DESEJADO.CSV)
#selectdata()
#CreateTable()
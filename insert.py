import sqlite3, csv


def importcsv(arq_csv):
    conn = sqlite3.connect('NuclearReactor.db')
    cursor = conn.cursor()
    with open(arq_csv, 'r') as arquivo:
        leitor_csv = csv.reader(arquivo)

        first_line = next(leitor_csv)  # Lê a 1ª linha da coluna e armazena

        for column in leitor_csv:
            if len(column) == len(first_line):  # Verifica se o número de colunas é válido
                #CRIA AS VARIAVEIS REFERENTES AS COLUNAS
                axlength = None
                rottrans = None
                nfp = None
                tipo = None
                rc1 = None
                zs1 = None
                r2c = None
                z2s = None
                b2c = None
                r_singularity = None
                d2_volume_d_psi2 = None
                b20_var = None
                etabar = None
                max_elong = None
                lgradb = None
                min_ro = None
                # VERIFICA SE CADA COLUNA EXISTE NO ARQUIVO CSV E SE EXISTIR CARREGA TODOS OS VALORES ASSOCIADOS NA VARIAVEL
                for x, item in enumerate(first_line):
                    if item.lower() == 'axlength' or item.lower() == 'axlenght':
                        axlength = column[x]
                    elif item.lower() == 'rottrans':
                        rottrans = column[x]
                    elif item.lower() == 'nfp':
                        nfp = column[x]
                    elif item.lower() == 'type' or item.lower() == 'heli' or item.lower() == 'helicity' or item.lower() == 'tipo':
                        tipo = column[x]
                    elif item.lower() == 'rc1' or item.lower() == 'r1c':
                        rc1 = column[x]
                    elif item.lower() == 'zs1' or item.lower() == 'z1s':
                        zs1 = column[x]
                    elif item.lower() == 'r2c' or item.lower() == 'rc2':
                        r2c = column[x]
                    elif item.lower() == 'z2s' or item.lower() == 'zs2':
                        z2s = column[x]
                    elif item.lower() == 'b2c' or item.lower() == 'bc2':
                        b2c = column[x]
                    elif item.lower() == 'r_singularity':
                        r_singularity = column[x]
                    elif item.lower() == 'd2_volume_d_psi2':
                        d2_volume_d_psi2 = column[x]
                    elif item.lower() == 'b20_var':
                        b20_var = column[x]
                    elif item.lower() == 'etabar' or item.lower() == 'eta':
                        etabar = column[x]
                    elif item.lower() == 'max_elong':
                        max_elong = column[x]
                    elif item.lower() == 'lgradb' or item.lower() == 'lgrad_gradb':
                        lgradb = column[x]
                    elif item.lower() == 'min_ro' or item.lower() == 'min_r0':
                        min_ro = column[x]
                    else:
                        print('Column not recognized:', item)

                if nfp is not None and tipo is not None:
                    if nfp.isdigit() and 1 <= int(nfp) <= 10 and (tipo == '1' or tipo.lower() == 'false' or tipo.lower() == 'qa'):
                        tipo = 1
                        cursor.execute(
                            "INSERT OR IGNORE INTO Omnigenous(axLength, RotTrans, nfp, Tipo, rc1, zs1, r2c, z2s, b2c, r_singularity, d2_volume_d_psi2, B20_var, etabar, max_elong, lgradB, min_RO) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                            (axlength, rottrans, nfp, tipo, rc1, zs1, r2c, z2s, b2c, r_singularity, d2_volume_d_psi2, b20_var,
                             etabar, max_elong, lgradb, min_ro))
                    elif nfp.isdigit() and 1 <= int(nfp) <= 10 and (tipo == '2' or tipo.lower() == 'true' or tipo.lower() == 'qh'):
                        tipo = 2
                        cursor.execute(
                            "INSERT OR IGNORE INTO Omnigenous(axLength, RotTrans, nfp, Tipo, rc1, zs1, r2c, z2s, b2c, r_singularity, d2_volume_d_psi2, B20_var, etabar, max_elong, lgradB, min_RO) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                            (axlength, rottrans, nfp, tipo, rc1, zs1, r2c, z2s, b2c, r_singularity, d2_volume_d_psi2, b20_var,
                             etabar, max_elong, lgradb, min_ro))
                    else:
                        print('Invalid insert')
                else:
                    print('Invalid number of columns:', len(column))

        conn.commit()
        print('Commit executed')

    conn.close()



def selectdata():
    conn = sqlite3.connect('NuclearReactor.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Omnigenous where r2c IS NOT NULL")
    data = cursor.fetchall()
    print('dados:')
    print("\n")
    for row in data:
        print(row)
        print("\n")
    conn.close()


importcsv('qsc_out.random_scan_nfp2_2ndorder.csv')
selectdata()

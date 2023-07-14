--CRIAÇÃO TABELA TIPO
Create TABLE Tipo(ID INTEGER PRIMARY KEY AUTOINCREMENT, DESC TEXT UNIQUE, DESC_TOTAL TEXT UNIQUE)

--CRIAÇÃO TABELA OMNIGENOUS
CREATE TABLE Omnigenous (
axLength float check(axLength>0),
RotTrans Float check(RotTrans>0),
nfp INTEGER check ( nfp between 1 and 10), --nfp so pode variar entre 1 e 10
Tipo integer REFERENCES Tipo(Tipo), -- Tipo está a fazer referência(no caso verifica se o valor inserido em Tipo está de acordo com o Tipos inseridos na tabela) à tabela Tipo
rc1 Float check(rc1 between -0.6 and 0.6), --rc1 tem de estar entre -0.6 e 0.6
zs1 Float check(zs1 between -0.6 and 0.6), -- zs1 tem de estar entre -0.6 e 0.6
rc2 Float check ( rc2 between -0.6 AND 0.6), -- rc2 tem de estar entre -0.6 e 0.6
zs2 float check (zs2 between -0.6 and 0.6), -- zs2 tem de estar entre -0.6 e 0.6
bc2 float check ( bc2 between -6 and -0.01), --bc2 tem de estar entre -0.6 e 0.6
r_singularity float,
d2_volume_d_psi2 float,
B20_var float,
etabar Float check(etabar between -6 and -0.01), --etabar tem de estar entre -6 e -0.01
max_elong float,
lgradB Float check(lgradB>0),
min_RO Float check ( min_RO>0));

Drop TABLE Omnigenous;

--CRIAR VIEW NA1
create view NA1 AS
    SELECT axLength, RotTrans,nfp,Tipo,rc1,zs1,etabar,max_elong,lgradB,min_RO FROM Omnigenous WHERE Tipo between 1 and 2 AND r2c IS NULL AND z2s IS NULL AND b2c IS NULL;

--CRIAR VIEW NA2
create view NA2 AS
    SELECT axLength, RotTrans,nfp,Tipo,rc1,zs1,rc2, zs2, bC2,etabar,max_elong,lgradB,min_RO FROM Omnigenous WHERE Tipo between 1 and 2 AND rc2 IS NOT NULL AND zs2 IS NOT NULL AND bc2 IS NOT NULL;

--CRIAR VIEW QA, Where Tipo == 1
create view QA AS SELECT * FROM Omnigenous WHERE Tipo == 1;

--CRIAR VIEW QH
CREATE VIEW QH AS SELECT * FROM Omnigenous WHERE Tipo == 2;



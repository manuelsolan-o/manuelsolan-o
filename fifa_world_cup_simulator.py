# Autor: Juan Manuel Hernรกndez Solano 
# Date: It is not finished yet but soon

# FIFA WORLD CUP SIMULATOR

import random 

clasificados = [ 
grupoA = [
'QATAR ๐ถ๐ฆ',
'ECUADOR ๐ช๐จ',
'SENEGAL ๐ธ๐ณ',
'PAรSES BAJOS ๐ณ๐ฑ'
],

grupoB = [
'INGLATERRA ๐ด๓ ง๓ ข๓ ฅ๓ ฎ๓ ง๓ ฟ',
'IRAN ๐ฎ๐ท',
'ESTADOS UNIDOS ๐บ๐ฒ',
'GALES ๐ด๓ ง๓ ข๓ ท๓ ฌ๓ ณ๓ ฟ' 
],

grupoC = [
'ARGENTINA ๐ฆ๐ท',
'ARABIA SAUDITA ๐ธ๐ฆ',
'MรXICO ๐ฒ๐ฝ',
'POLONIA ๐ต๐ฑ'
],

grupoD = [
'FRANCIA ๐ซ๐ท',
'AUSTRALIA ๐ฆ๐บ',
'DINAMARCA ๐ฉ๐ฐ',
'TรNEZ ๐น๐ณ'
],

grupoE = [
'ESPAรA ๐ช๐ฆ',
'COSTA RICA ๐จ๐ท',
'ALEMANIA ๐ฉ๐ช',
'JAPรN ๐ฏ๐ต'
],

grupoF = [
'BรLGICA ๐ง๐ช',
'CANADร ๐จ๐ฆ',
'MARRUECOS ๐ฒ๐ฆ',
'CROACIA ๐ญ๐ท'
],

grupoG = [
'BRASIL ๐ง๐ท',
'SERBIA ๐ท๐ธ',
'SUIZA ๐จ๐ญ',
'CAMERรN ๐จ๐ฒ'
],

grupoH = [
'PORTUGAL ๐ต๐น',
'GHANA ๐ฌ๐ญ',
'URUGUAY ๐บ๐พ',
'COREA DEL SUR ๐ฐ๐ท'
]
  
goles = list(range(1,6))

"""
////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                GRUPO A
///////////////////////////////////////////////////////////////////////////////////////////////////////

"""

grupoA = [
'QATAR ๐ถ๐ฆ',
'ECUADOR ๐ช๐จ',
'SENEGAL ๐ธ๐ณ',
'PAรSES BAJOS ๐ณ๐ฑ'
]
puntosQatar = 0
golesQatar = 0

puntosEcuador = 0
golesEcuador = 0

puntosSenegal = 0
golesSenegal = 0

puntosPBajos = 0 
golesPBajos = 0

print('FASE DE GRUPOS GRUPO A\n')

for g in range(1,4):

    if grupoA[g] == 'ECUADOR ๐ช๐จ':
        golesQatar = random.choice(goles)
        golesEcuador = random.choice(goles)

        print(f'{grupoA[0]} {golesQatar} vs {grupoA[g]} {golesEcuador}')

        if golesQatar > golesEcuador:
            puntosQatar += 3
            print('\nGANA QATAR ๐ถ๐ฆ\n')

        elif golesEcuador > golesQatar:
            puntosEcuador += 3
            print('\nGANA ECUADOR ๐ช๐จ\n')

        else:
            puntosQatar += 1
            puntosEcuador += 1
            print('\nEMPATE\n')


    elif grupoA[g] == 'SENEGAL ๐ธ๐ณ':
        golesQatar = random.choice(goles)
        golesSenegal = random.choice(goles)

        print(f'{grupoA[0]} {golesQatar} vs {grupoA[g]} {golesSenegal}')

        if golesQatar > golesSenegal:
            puntosQatar += 3
            print('\nGANA QATAR ๐ถ๐ฆ\n')

        elif golesSenegal > golesQatar:
            puntosSenegal += 3
            print('\nGANA SENEGAL ๐ธ๐ณ\n')

        else:
            puntosQatar += 1
            puntosSenegal += 1
            print('\nEMPATE\n')

    elif grupoA[g] == 'PAรSES BAJOS ๐ณ๐ฑ':
        golesQatar = random.choice(goles)
        golesPBajos = random.choice(goles)

        print(f'{grupoA[0]} {golesQatar} vs {grupoA[g]} {golesPBajos}')

        if golesQatar > golesPBajos:
            puntosQatar += 3
            print('\nGANA QATAR ๐ถ๐ฆ\n')

        elif golesPBajos > golesQatar:
            puntosPBajos += 3
            print('\nGANA PAรSES BAJOS ๐ณ๐ฑ\n')

        else:
            puntosQatar += 1
            puntosPBajos += 1
            print('\nEMPATE\n')

for g in range(2,4):

    if grupoA[g] == 'SENEGAL ๐ธ๐ณ':
        golesEcuador = random.choice(goles)
        golesSenegal = random.choice(goles)

        print(f'{grupoA[1]} {golesEcuador} vs {grupoA[g]} {golesSenegal}')

        if golesEcuador > golesSenegal:
            puntosEcuador += 3
            print('\nGANA ECUADOR ๐ช๐จ\n')

        elif golesSenegal > golesEcuador:
            puntosSenegal += 3
            print('\nGANA SENEGAL ๐ธ๐ณ\n')

        else:
            puntosEcuador += 1
            puntosSenegal += 1
            print('\nEMPATE\n')

    elif grupoA[g] == 'PAรSES BAJOS ๐ณ๐ฑ':
        golesEcuador = random.choice(goles)
        golesPBajos = random.choice(goles)

        print(f'{grupoA[1]} {golesEcuador} vs {grupoA[g]} {golesPBajos}')

        if golesEcuador > golesPBajos:
            puntosEcuador += 3
            print('\nGANA ECUADOR ๐ช๐จ\n')

        elif golesPBajos > golesEcuador:
            puntosPBajos += 3
            print('\nGANA PAรSES BAJOS ๐ณ๐ฑ\n')

        else:
            puntosEcuador += 1
            puntosPBajos += 1
            print('\nEMPATE\n')


for g in range(3,4):

    if grupoA[g] == 'PAรSES BAJOS ๐ณ๐ฑ':
        golesSenagal = random.choice(goles)
        golesPBajos = random.choice(goles)

        print(f'{grupoA[2]} {golesSenagal} vs {grupoA[g]} {golesPBajos}')

        if golesSenagal > golesPBajos:
            puntosSenegal += 3
            print('\nGANA SENEGAL ๐ธ๐ณ\n')

        elif golesPBajos > golesSenagal:
            puntosPBajos += 3
            print('\nGANA PAรSES BAJOS ๐ณ๐ฑ\n')

        else:
            puntosSenegal += 1
            puntosPBajos += 1
            print('\nEMPATE\n')

puntos_grupoA = {
'QATAR ๐ถ๐ฆ':puntosQatar,
'ECUADOR ๐ช๐จ':puntosEcuador,
'SENEGAL ๐ธ๐ณ':puntosSenegal,
'PAรSES BAJOS ๐ณ๐ฑ':puntosPBajos}

sort_grupoA = sorted(puntos_grupoA.items(), key=lambda x: x[1], reverse=True)

pasa_GrupoA = [] 
print(f'\nTABLA GRUPO A\n')
for k,v in sort_grupoA:
    print(f'{k} : {v}   PUNTOS ')
    pasa_GrupoA.append(k)

print(f'\nAVANZAN {pasa_GrupoA[0]} Y {pasa_GrupoA[1]}\n')  
  
grupoB = [
'INGLATERRA ๐ด๓ ง๓ ข๓ ฅ๓ ฎ๓ ง๓ ฟ',
'IRAN ๐ฎ๐ท',
'ESTADOS UNIDOS ๐บ๐ฒ',
'GALES ๐ด๓ ง๓ ข๓ ท๓ ฌ๓ ณ๓ ฟ' 
]
puntosInglaterra = 0
golesInglaterra = 0

puntosIran = 0
golesIran = 0

puntosEU = 0
golesEU = 0

puntosGales = 0 
golesGales = 0

goles = list(range(1,6))

print('FASE DE GRUPOS GRUPO B\n')

for g in range(1,4):

    if grupoB[g] == 'IRAN ๐ฎ๐ท':
        golesInglaterra = random.choice(goles)
        golesIran = random.choice(goles)

        print(f'{grupoB[0]} {golesInglaterra} vs {grupoB[g]} {golesIran}')

        if golesInglaterra > golesIran:
            puntosInglaterra += 3
            print('\nGANA INGLATERRA ๐ด๓ ง๓ ข๓ ฅ๓ ฎ๓ ง๓ ฟ\n')

        elif golesIran > golesInglaterra:
            puntosIran += 3
            print('\nGANA IRAN ๐ฎ๐ท\n')

        else:
            puntosInglaterra += 1
            puntosIran += 1
            print('\nEMPATE\n')


    elif grupoB[g] == 'ESTADOS UNIDOS ๐บ๐ฒ':
        golesInglaterra = random.choice(goles)
        golesEU = random.choice(goles)

        print(f'{grupoB[0]} {golesInglaterra} vs {grupoB[g]} {golesEU}')

        if golesInglaterra > golesEU:
            puntosInglaterra += 3
            print('\nGANA INGLATERRA ๐ด๓ ง๓ ข๓ ฅ๓ ฎ๓ ง๓ ฟ\n')

        elif golesEU > golesInglaterra:
            puntosEU += 3
            print('\nGANA ESTADOS UNIDOS ๐บ๐ฒ\n')

        else:
            puntosInglaterra += 1
            puntosEU += 1
            print('\nEMPATE\n')

    elif grupoB[g] == 'GALES ๐ด๓ ง๓ ข๓ ท๓ ฌ๓ ณ๓ ฟ':
        golesInglaterra = random.choice(goles)
        golesEU = random.choice(goles)

        print(f'{grupoB[0]} {golesInglaterra} vs {grupoB[g]} {golesGales}')

        if golesInglaterra > golesGales:
            puntosInglaterra += 3
            print('\nGANA INGLATERRA ๐ด๓ ง๓ ข๓ ฅ๓ ฎ๓ ง๓ ฟ\n')

        elif golesGales > golesInglaterra:
            puntosGales += 3
            print('\nGANA GALES ๐ด๓ ง๓ ข๓ ท๓ ฌ๓ ณ๓ ฟ\n')

        else:
            puntosInglaterra += 1
            puntosEU += 1
            print('\nEMPATE\n')

for g in range(2,4):

    if grupoB[g] == 'ESTADOS UNIDOS ๐บ๐ฒ':
        golesIran = random.choice(goles)
        golesEU = random.choice(goles)

        print(f'{grupoB[1]} {golesIran} vs {grupoB[g]} {golesEU}')

        if golesIran > golesEU:
            puntosIran += 3
            print('\nGANA IRAN ๐ฎ๐ท\n')

        elif golesEU > golesIran:
            puntosEU += 3
            print('\nGANA ESTADOS UNIDOS ๐บ๐ฒ\n')

        else:
            puntosIran += 1
            puntosEU += 1
            print('\nEMPATE\n')

    elif grupoB[g] == 'GALES ๐ด๓ ง๓ ข๓ ท๓ ฌ๓ ณ๓ ฟ':
        golesIran = random.choice(goles)
        golesGales = random.choice(goles)

        print(f'{grupoB[1]} {golesIran} vs {grupoB[g]} {golesGales}')

        if golesIran > golesGales:
            puntosIran += 3
            print('\nGANA IRAN ๐ฎ๐ท\n')

        elif golesIran > golesGales:
            puntosGales += 3
            print('\nGANA GALES ๐ด๓ ง๓ ข๓ ท๓ ฌ๓ ณ๓ ฟ\n')

        else:
            puntosIran += 1
            puntosGales += 1
            print('\nEMPATE\n')


for g in range(3,4):

    if grupoB[g] == 'GALES ๐ด๓ ง๓ ข๓ ท๓ ฌ๓ ณ๓ ฟ':
        golesEU = random.choice(goles)
        golesGales = random.choice(goles)

        print(f'{grupoB[2]} {golesEU} vs {grupoB[g]} {golesGales}')

        if golesEU > golesGales:
            puntosEU += 3
            print('\nGANA ESTADOS UNIDOS ๐บ๐ฒ\n')

        elif golesGales > golesEU:
            puntosGales += 3
            print('\nGANA GALES ๐ด๓ ง๓ ข๓ ท๓ ฌ๓ ณ๓ ฟ\n')

        else:
            puntosEU += 1
            puntosGales += 1
            print('\nEMPATE\n')

puntos_grupoB = {
'INGLATERRA ๐ด๓ ง๓ ข๓ ฅ๓ ฎ๓ ง๓ ฟ':puntosInglaterra,
'IRAN ๐ฎ๐ท': puntosIran,
'ESTADOS UNIDOS ๐บ๐ฒ': puntosEU,
'GALES ๐ด๓ ง๓ ข๓ ท๓ ฌ๓ ณ๓ ฟ':puntosGales }

sort_grupoB = sorted(puntos_grupoB.items(), key=lambda x: x[1], reverse=True)

pasa_GrupoB = [] 
print(f'\nTABLA GRUPO B\n')
for k,v in sort_grupoB:
    print(f'{k} : {v}   PUNTOS ')
    pasa_GrupoB.append(k)

print(f'\nAVANZAN {pasa_GrupoB[0]} Y {pasa_GrupoB[1]}\n')
  
grupoC = [
'ARGENTINA ๐ฆ๐ท',
'ARABIA SAUDITA ๐ธ๐ฆ',
'MรXICO ๐ฒ๐ฝ',
'POLONIA ๐ต๐ฑ'
]
puntosArgentina = 0
golesArgentina = 0

puntosArabia = 0
golesArabia = 0

puntosMex = 0
golesMex = 0

puntosPolonia = 0 
golesPolonia = 0

goles = list(range(1,6))

print('FASE DE GRUPOS GRUPO C\n')

for g in range(1,4):

    if grupoC[g] == 'ARABIA SAUDITA ๐ธ๐ฆ':
        golesArgentina = random.choice(goles)
        golesArabia = random.choice(goles)

        print(f'{grupoC[0]} {golesArgentina} vs {grupoC[g]} {golesArabia}')

        if golesArgentina > golesArabia:
            puntosArgentina += 3
            print('\nGANA ARGENTINA ๐ฆ๐ท\n')

        elif golesArabia > golesArgentina:
            puntosArabia += 3
            print('\nGANA ARABIA SAUDITA ๐ธ๐ฆ\n')

        else:
            puntosArgentina += 1
            puntosArabia += 1
            print('\nEMPATE\n')


    elif grupoC[g] == 'MรXICO ๐ฒ๐ฝ':
        golesArgentina = random.choice(goles)
        golesMex = random.choice(goles)

        print(f'{grupoC[0]} {golesArgentina} vs {grupoC[g]} {golesMex}')

        if golesArgentina > golesMex:
            puntosArgentina += 3
            print('\nGANA ARGENTINA ๐ฆ๐ท\n')

        elif golesMex > golesArgentina:
            puntosMex += 3
            print('\nGANA MรXICO ๐ฒ๐ฝ\n')

        else:
            puntosArgentina += 1
            puntosMex += 1
            print('\nEMPATE\n')

    elif grupoC[g] == 'POLONIA ๐ต๐ฑ':
        golesArgentina = random.choice(goles)
        golesPolonia = random.choice(goles)

        print(f'{grupoC[0]} {golesArgentina} vs {grupoC[g]} {golesPolonia}')

        if golesArgentina > golesPolonia:
            puntosArgentina += 3
            print('\nGANA ARGENTINA ๐ฆ๐ท\n')

        elif golesPolonia > golesArgentina:
            puntosPolonia += 3
            print('\nGANA POLONIA ๐ต๐ฑ\n')

        else:
            puntosArgentina += 1
            puntosPolonia += 1
            print('\nEMPATE\n')

for g in range(2,4):

    if grupoC[g] == 'MรXICO ๐ฒ๐ฝ':
        golesArabia = random.choice(goles)
        golesMex = random.choice(goles)

        print(f'{grupoC[1]} {golesArabia} vs {grupoC[g]} {golesMex}')

        if golesArabia > golesMex:
            puntosArabia += 3
            print('\nGANA ARABIA SAUDITA ๐ธ๐ฆ\n')

        elif golesMex > golesArabia:
            puntosMex += 3
            print('\nGANA MรXICO ๐ฒ๐ฝ\n')

        else:
            puntosArabia += 1
            puntosMex += 1
            print('\nEMPATE\n')

    elif grupoC[g] == 'POLONIA ๐ต๐ฑ':
        golesArabia = random.choice(goles)
        golesPolonia = random.choice(goles)

        print(f'{grupoC[1]} {golesArabia} vs {grupoC[g]} {golesPolonia}')

        if golesArabia > golesPolonia:
            puntosArabia += 3
            print('\nGANA ARABIA SAUDITA ๐ธ๐ฆ\n')

        elif golesIran > golesGales:
            puntosPolonia += 3
            print('\nGANA POLONIA ๐ต๐ฑ\n')

        else:
            puntosArabia += 1
            puntosPolonia += 1
            print('\nEMPATE\n')


for g in range(3,4):

    if grupoC[g] == 'POLONIA ๐ต๐ฑ':
        golesMex = random.choice(goles)
        golesPolonia = random.choice(goles)

        print(f'{grupoC[2]} {golesMex} vs {grupoC[g]} {golesPolonia}')

        if golesMex > golesPolonia:
            puntosMex += 3
            print('\nGANA MรXICO ๐ฒ๐ฝ\n')

        elif golesPolonia > golesMex:
            puntosPolonia += 3
            print('\nGANA POLONIA ๐ต๐ฑ\n')

        else:
            puntosMex += 1
            puntosPolonia += 1
            print('\nEMPATE\n')

puntos_grupoC = {
'ARGENTINA ๐ฆ๐ท':puntosArgentina,
'ARABIA SAUDITA ๐ธ๐ฆ':puntosArabia,
'MรXICO ๐ฒ๐ฝ':puntosMex,
'POLONIA ๐ต๐ฑ':puntosPolonia }

sort_grupoC = sorted(puntos_grupoC.items(), key=lambda x: x[1], reverse=True)

pasa_GrupoC = [] 
print(f'\nTABLA GRUPO C\n')
for k,v in sort_grupoC:
    print(f'{k} : {v}   PUNTOS ')
    pasa_GrupoC.append(k)

print(f'\nAVANZAN {pasa_GrupoC[0]} Y {pasa_GrupoC[1]}\n')
 
# it will be finished soon hehe

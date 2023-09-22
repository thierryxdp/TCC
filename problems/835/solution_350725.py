def melhor_volta(matriz):
    """Recebe uma matriz, com os tempos em segundos dos corredores em cada volta.
    Retorna de quem foi a melhor volta, com qual tempo e em que volta; list -> tupla"""
    corredor1 = matriz[0]
    corredor2 = matriz[1]
    corredor3 = matriz[2]
    corredor4 = matriz[3]
    corredor5 = matriz[4]
    corredor6 = matriz[5]
    contador = 1
    if min(corredor1) < min(corredor2) and min(corredor3) and min(corredor4) and min(corredor5) and min(corredor6):
        while contador < 10:
            if corredor1[contador] == min(corredor1)
                return 1,corredor1[contador],contador
            contador += 1
    elif min(corredor2) < min(corredor1) and min(corredor3) and min(corredor4) and min(corredor5) and min(corredor6):
        while contador < 10:
            if corredor1[contador] == min(corredor1)
                return 2,corredor2[contador],contador
            contador += 1
    elif min(corredor3) < min(corredor2) and min(corredor1) and min(corredor4) and min(corredor5) and min(corredor6):
        while contador < 10:
            if corredor1[contador] == min(corredor1)
                return 3,corredor3[contador],contador
            contador += 1
    elif min(corredor4) < min(corredor2) and min(corredor3) and min(corredor1) and min(corredor5) and min(corredor6):
        while contador < 10:
            if corredor1[contador] == min(corredor1)
                return 4,corredor4[contador],contador
            contador += 1
    elif min(corredor5) < min(corredor2) and min(corredor3) and min(corredor4) and min(corredor1) and min(corredor6):
        while contador < 10:
            if corredor1[contador] == min(corredor1)
                return 5,corredor5[contador],contador
            contador += 1
    elif min(corredor6) < min(corredor2) and min(corredor3) and min(corredor4) and min(corredor5) and min(corredor1):
        while contador < 10:
            if corredor1[contador] == min(corredor1)
                return 6,corredor6[contador],contador
            contador += 1
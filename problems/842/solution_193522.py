def pontos_por_time(L1, L2):
    '''
    dados os resultados de duas partidas entre
    Cormengo e Flamínthians, determina a quantidade
    de pontos acumulada por cada uma das duas equipes
    
    a ordem dos elementos de ambas as listas deve ser
    [gols do cormengo, gols do flamínthians]
    
    função:
    list, list -> dictionary
    
    entradas das listas:
    int, int
    '''
    if L1[0]>L1[1] && L2[0]>L2[1]:
        resultado = {
            "Cormengo" : 6,
            "Flamínthians" : 0
        }
        return resultado
    elif L1[0]>L1[1] && L2[0]==L2[1]:
        resultado = {
            "Cormengo" : 4,
            "Flamínthians" : 1
        }
        return resultado
    elif (L1[0]>L1[1] && L2[0]<L2[1]) or (L1[0]<L1[1] && L2[0]>L2[1]):
        resultado = {
            "Cormengo" : 3,
            "Flamínthians" : 3
        }
        return resultado
    elif L1[0]<L1[1] && L2[0]==L2[1]:
        resultado = {
            "Cormengo" : 1,
            "Flamínthians" : 4
        }
        return resultado
    elif L1[0]<L1[1] && L2[0]<L2[1]:
        resultado = {
            "Cormengo" : 0,
            "Flamínthians" : 6
        }
        return resultado
    else:
        retultado = {
            "Cormengo" : 2,
            "Flamínthians" :2
        }
        return resultado
def melhor_volta(matriz):
    """Função que receba uma matriz 6x10 com os tempos em segundo dos corredores 
    em cada volta, retornando uma tupla informando de quem foi a melhor volta da 
    prova, em qual tempo e em que volta; list=> tuple"""
    tm = []
    for linha in matriz:
        tM = min(linha)
        list.append(tm,tM)
    time = min(tm)
    corredor = list.index(tm,time) + 1
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            if time == matriz[linha][coluna]:
                v = coluna + 1
    return (corredor,time,v)
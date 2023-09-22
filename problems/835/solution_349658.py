def melhor_volta(matriz):
    """ Dada uma matriz com os tempos em segundos de cada corredor de Kart em cada volta e retorna uma tupla com quem fez a melhor volta, em que tempo, em que volta;
    list->tuple"""
    lista=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            lista.append(matriz[i][j])
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if min(lista) in [matriz[i][j]]:
                return i+1,min(lista),j+1
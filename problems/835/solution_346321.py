def melhor_volta(matriz):
    '''retorna uma tupla informando de quem foi a melhor volta, com qual tempo e em que volta.lista->tupla'''
    tempo=[]
    for i in range(len(matriz)):
        list.append(tempo,min(matriz[i]))
    return (list.index(tempo,min(tempo))+1,min(tempo),list.index(matriz[list.index(tempo,min(tempo))],min(tempo))
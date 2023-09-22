def melhor_volta (matriz):
    '''retona quem foi a melhor volta da prova, com qual tempo e em que volta'''
    '''list[list] -> tuple'''
    
    lista = []
    vencedor = ()
    for i in range(len(matriz)):
        list.append(lista,min(matriz[i]))
    tempo = min(lista)
    compet = list.index(lista, tempo)
    final = list.indez(matriz[compet],tempo)
    vencedor = (compet+1, tempo, final+1)
    return vencedor
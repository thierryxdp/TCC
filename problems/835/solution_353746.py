def melhor_volta (matriz):
    '''função que dada uma matriz com tempos em segundos das voltas de cada corredor retorna de quem foi a melhor
    volta, com qual tempo e em que volta; list->tuple'''
    i=0
    lista = []
    for elem in matriz:
        lista += sum(elem[i])
    i+=1
    return lista
def melhor_volta(matriz):
    '''Dada uma matriz 6x10 com tempos
       de corredores em cada volta. A 
       funcao retorna de quem foi a melhor
       volta, com qual tempo e em que volta;
       list -> int, int, int'''
    i = 0 
    lista_min = []
    while i < len(matriz):
        valor_min = min(matriz[i])
        posicao = matriz[i].index(min(matriz[i]))
        lista_min = [valor_min] + lista_min
        i = i+1 
    return (min(lista_min), posicao)
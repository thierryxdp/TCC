def melhor_volta(matriz):
    """Recebe uma matriz contendo o tempo de cada corredor
    nas 10 voltas e retorna uma tupla informando quem deu 
    a melhor volta, o tempo e em que volta;
    list -> tuple"""
    n_linhas = len(matriz)
    menores_tempos= []
    for i in range(n_linhas):
        list.append(menores_tempos,min(matriz[i]))
    menor_tempo= min(menores_tempos)
    
    corredor= 1 + list.index(matriz, min(matriz))
    volta= list.index(matriz[corredor-1],menor_tempo)
    
    return (corredor, menor_tempo, volta)
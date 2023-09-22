def melhor_volta(matriz):
    """
    Função que recebe uma matriz 6x10 com as informações dos tempos
    de uma corrida de Kart de 6 corredores e retorna uma tupla contendo
    qual corredor teve a melhor volta, qual foi o tempo dessa volta e
    qual foi o número dessa volta.
    
    list --> tuple
    """
    melhores_voltas=[]
    
    for i in matriz:
        
        melhores_voltas.append(min(i))

    melhor_corredor=melhores_voltas.index(min(melhores_voltas))+1
    melhor_tempo=min(melhores_voltas)
    melhor_volta=matriz[melhor_corredor-1].index(melhor_tempo)+1
    return melhor_corredor,melhor_tempo,melhor_volta
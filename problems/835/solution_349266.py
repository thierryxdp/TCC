def melhor_volta(matriz):
    ''' retorna qual o melhor corredor, melhor tempo e melhor volta
    list -> tuple
    '''
    lista = []
    for i in matriz:
        for k in i:
            lista.append(k)
            melhor_tempo = min(lista)
            if melhor_tempo in i:
                resultado = (matriz.index(i)+1, melhor_tempo, i.index(melhor_tempo)+1) 
    return resultado
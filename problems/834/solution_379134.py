def media_matriz(matriz):
    '''A função recebe uma matriz de numeros inteiros
        como parametro e devolve a média de cada numero;
        list --> list        
    '''
    media = []
    i = 0
    for numero in  matriz:
        for numero in matriz[i]:
            list.append(media,numero)
        i+=1           
    return round(sum(media)/len(media),2)
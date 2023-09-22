def media_matriz(matriz):
    '''A função recebe uma matriz de numeros inteiros
        como parametro e devolve a média total dos numeros;
        list --> float       
    '''
    media = []
    i = 0
    for numero in  matriz:
        for numero in matriz[i]:
            list.append(media,numero)
        i+=1           
    return round(sum(media)/len(media),2)
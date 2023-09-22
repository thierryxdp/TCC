def divide_num(n,x):
    '''retorna n/x; int, int -> float'''
    return n/x
def media_matriz(matriz):
    '''retorna a media e todos os numeros da matriz; list -> float'''
    n1=len(matriz)
    n2=len(matriz[0])
    n_total=n1*n2
	lista_numeros=[]
    for x in range(len(matriz)):
        for y in range(len(matriz[x])):
            lista_numeros.append(matriz[x][y])
    medias=list(map(divide_num,lista_numeros,n_total*[n_total]))
    
    return medias
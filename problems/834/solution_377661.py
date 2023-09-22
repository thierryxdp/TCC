def media_matriz(matriz):
    '''Funcao que retorna a media de todos os numeros da matriz de entrada
	com duas casas decimais de precisao.
    list->float'''
    x=0
    total=0
    soma=0
    while x in range(len(matriz)):
        total=total+len(matriz[x])
        soma=soma+sum(matriz[x])
        x=x+1
    return round(soma/total,2)
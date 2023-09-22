def repetidos(lista):
    '''Recebe como entrada uma lista de números, retornando o 
    número de vezes que um elemento da lista é igual ao elemento 
    anterior.
    list[int] -> int'''
	posicao=0
    contador=0
    valor_anterior,valor=-1,-1
    while posicao<len(lista):
        valor=lista[posicao]
        if valor==valor_anterior:
            contador=contador+1
        valor_anterior=valor
        posicao=posicao+1
    return contador
def eh_quadrada(matriz):
    '''verifica se a matriz é quadrada
    list--> bool'''

    contador = 0  #inicia contador em zero

    if len(matriz) == 0:  #se a matriz não tiver elementos:
        return True  #retornar verdadeiro
    
    for item in matriz:  #para cada item da matriz:
        if len(item) == len(matriz):  #se tamanho do item for igual ao tamanho da matriz:
            contador += 1  #incrementa contador

    if contador == len(matriz):  #se contador for igual ao tamanho da matriz
        return True  #retorna verdadeiro
    else:
        return False  #retorna falso
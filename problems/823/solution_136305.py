def faltante(lista):
    posicao=0
    while lista[posicao] < len(lista):
        if posicao+1 == lista[posicao]:
        	posicao = posicao + 1
    return posicao
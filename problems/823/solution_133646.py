def faltante(lista):
    """	Função que ao receber uma lista com números inteiros de 1 a N,
    retorna o número inteiro que está faltando
    list -> int"""
    i = 0
    contador = 0
    while i < len(lista):
        if i+1 == lista[i]:
            contador+=1
    	i +=1
    return contador + 1
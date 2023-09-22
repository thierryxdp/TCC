def faltante(lista):
    """dada uma lista com N − 1 inteiros numerados de 1 a N, a função descobre qual número inteiro deste intervalo está faltando.
    parâmetro de entrada é uma lista L de tamanho N − 1 contendo números inteiros (não repetidos) de 1 a N.
    A função  retorna o número inteiro x que pertence ao intervalo [1, N] mas que não pertence a lista de entrada L. (o número que está faltando)
    
    entrada-> list de números inteiros ordenados
    retorna-> int"""
    
    numero=lista [0]
    indice=1
    
    while numero == lista[indice-1]:
        indice=indice+1
        numero = numero+1
        
    return numero
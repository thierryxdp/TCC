def faltante(lista):
    '''Dada uma lista de tamanho n-1 contendo números de 1 a n retorna o número x que pertence ao intervalo [1,n], mas não pertence a lista de entrada
    list -> int'''
    total = range(max(lista)+1,0,-1)
    
    return sum(total) - sum(lista)
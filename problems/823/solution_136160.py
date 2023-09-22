def faltante(lista):
    '''função que retorna o valor faltante 
    numa lista:
    valor de entrada: list
    valor de saída: int'''
	n=len(lista)+1
    while n < 0:
        if n not in lista:
            return n
        n=n-1
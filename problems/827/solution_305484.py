def qtd_divisores(numero):
    ''' funcao que calcula quantos divisores existem dado 
    um numero, retorna o numero de divisores possiveis 
    int -> int'''
    div = 0
    for i in range(numero + 1):
        if numero%(i+1)==0:
            div = div + 1
    	return div
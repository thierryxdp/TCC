def faltante(lista):
    '''funcao que retorna qual o numero da peca faltante em um intervalo de 1 a N, dada uma lista com N-1 inteiros
    lista->int'''
    n=1
    i=0
    while i<len(lista):
        while n in lista:
            n=n+1
        i=i+1
  	return n
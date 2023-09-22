def faltante(l):
	    '''Recebe uma lista de tamanho n-1 contendo apenas numeros inteiros nao 
	    repetidos de 1 a n e retorna o numero inteiro que pertence ao intervalo
	    [1,N] mas que esta faltando na lista de entrada;
	    list -> int'''
	    list.sort(l)
	    cnt=0
	    lista=list(range(len(l)+1))
	    while cnt<len(l):
	        if lista[cnt+1] == l[cnt]:
	            cnt=cnt+1
	        if lista[cnt] != l[cnt-1]:
	            cnt=cnt
        if lista[cnt]==len(l):
            return lista[cnt]+1
        else:
            return lista[cnt]+1
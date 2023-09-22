filtra_pares(tupla):
    '''Funcao que recebe uma tupla com quatro numeros inteiros e
    retorna uma tupla com somente os numeros pares.
    Entrada: tuple(int, int, int, int)'''
    n1=tupla[0] ; n2=tupla[1] ; n3=tupla[2] ; n4=tupla[3]	
    vazio=()
    if n1%2==0:
	    x1=tupla[:1]
    if n2%2==0:
	    x2=tupla[1:2]
    if n3%2==0:
	    x3=tupla[2:3]
    if n4%2==0:
	    x4=tupla[3:]

    if n1%2!=0:
	    x1=vazio
    if n2%2!=0:
	    x2=vazio
    if n3%2!=0:
	    x3=vazio
    if n4%2!=0:
	    x4=vazio

    saida=()
    saida=x1
    saida+=x2
    saida+=x3
    saida+=x4

    return saida
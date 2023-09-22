def filtra_pares(x):
    '''Função que recebe como entrada uma tupla de quatro elementos inteiros
    e retorna uma nova tupla somente com os valores pares presentes na tupla
    anterior.
    tupla -> tupla'''
    n_pares = ()
    if x[0]%2==0:
        n_pares = n_pares + (x[0], , , )
    elif x[1]%2==0:
        n_pares = n_pares + (x[1], , , )
    elif x[2]%2==0:
        n_pares = n_pares + (x[2], , , )
    elif x[3]%2==0:
        n_pares = n_pares + (x[3], , , )
    	return n_pares
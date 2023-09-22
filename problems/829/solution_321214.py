def soma_h(n):
    '''Retorna a soma da serie harmonica ate denominador dado n
	int->float'''
    H=0
    for i in range(1,n+1):
        H+=(1/i)
    return round(H,2)
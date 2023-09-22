def soma_h(n):
    '''função que dado um inteiro n calcula o valor de H com duas casas
    decimais, onde h é a soma dos inversos de 1 até n; 
    int-->float'''
    H=0
    for numero in range(1,n+1):
	    H=H+(1/numero)
    return round(H,2)
def filtra_pares(x):
    '''Função que recebae uma tupla com quatro elementos inteiros como parâmetro,
    e retorna uma nova tupla contendo apenas os elementos pares da tupla original,
    na mesma ordem em que se encontravam. 
    Paramentros de entrada: tipo tupla(int,int,int,int)
    Retorno: tipo tupla
    '''
    p=q=r=s=()
    if (x[0]%2==0):
		p=x[0]
    if (x[1]%2==0):
    	q=x[1]
    if (x[2]%2==0):
   		r=x[2]
    if (x[3]%2==0):
    	s=x[3]
    t=(p,q,r,s)
    return t
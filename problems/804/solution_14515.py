def filtra_pares(x):
    '''Função que recebae uma tupla com quatro elementos inteiros como parâmetro,
    e retorna uma nova tupla contendo apenas os elementos pares da tupla original,
    na mesma ordem em que se encontravam. 
    Paramentros de entrada: tipo tupla(int,int,int,int)
    Retorno: tipo tupla
    '''
    p=x[0]
    q=x[1]
    r=x[2]
    s=x[3]
    t=()
    if not (p%2==0):
    	p=()
    if not(q%2==0):
    	q=()
    if not(r%2==0):
    	r=()
    if not(s%2==0):
    	s=()
    return p,q,r,s
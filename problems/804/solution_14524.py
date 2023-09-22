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
    t=[]
    if (p%2==0):
    	t=t+x[0]
    if (q%2==0):
    	t=t+x[0]
    if (r%2==0):
   		t=t+x[0]
    if (s%2==0):
    	t=t+x[0]
    return t
def soma_h(n:int)-> float:
    '''Função chamada soma h para calcular e retornar o valor H com N termos'''
   	h=0
    for i in range(1,n+1):
    	h=h+(1/i)
   	return round(h,2)
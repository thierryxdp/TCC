def qtd_divisores(n):
    '''retorna quantos divisore um num tem
    int -> int'''
    
    lista = []
    num = n
    
    
    
    
    
    
    
    for i in range(1,n+1):
		if num%i==0:
      	  lista.append(i)
    return len(lista)
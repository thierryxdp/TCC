def qtd_divisores(n:int) ->int:
    
    lista = list()
    for i in range(n+1):
        if i>=1:
        	if (n/i)%1 == 0:
           		lista.append(i) 
    return len(lista)
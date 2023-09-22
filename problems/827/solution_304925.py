def qtd_divisores(n:int) ->int:
    x = 0
    lista = list()
    for i in range(n+1):
        if i>=1:
        	if x%i == 0:
           		lista.append(i)
    		x += 1
    return lista
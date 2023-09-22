def qtd_divisores(n):
    lista=[]
    for i in range(2:(n+1)) :
        if i%n:
            lista+= n
   	return lista
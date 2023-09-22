def qtd_divisores(n):
    '''retorna a quantidade de divisores do numero de entrada
    int->int'''
    listadivisores=[]
   	
	for num in range(1,n+1):
        if n%num==0:
            listadivisores+=(num,)
   		return len(listadivisores)
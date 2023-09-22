def primo(n):
    '''retorna a quantidade de divisores do numero de entrada
    int->int'''
    listadivisores=[]
   	
	for num in range(1,n+1):
        if n%num==0:
            listadivisores+=[num,]
            if len(listadivisores)>2 or n==1:
        		return False
    		if len(listadivisores)==2:
        		return True
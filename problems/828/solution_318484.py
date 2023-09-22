def primo(n):
    '''retorna se o numero de entrada é primo ou nao
    int->bool'''
    listadivisores=[]
   	
	for num in range(1,n+1):
        if n%num==0:
            listadivisores+=[num,]
            if len(listadivisores)>2 or n==1:
        		return False
    		elif len(listadivisores)==2 and num==n:
        		return True
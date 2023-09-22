def divisores(n):
    '''retorna os divisores do numero de entrada
    int->int'''
    listadivisores=[]
   	
	for num in range(1,n+1000000):
        if n%num==0:
            listadivisores+=[num,]
    return listadivisores

def primo(n):
    
    for num in divisores(n):
        if num%n==0:
            return True
        else:
            return False
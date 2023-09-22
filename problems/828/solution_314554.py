def primo(n):
    '''retorna se o numero é primo ou nao
   	int->bool'''
    lista= range(1,n+1)
    for num in lista:
       	if num/1==n and num%n==0:
            return True
        
        else:
            return False
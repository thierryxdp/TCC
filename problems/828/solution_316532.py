def primo(n):
    '''Função que recebe um número inteiro positivo e retorna True
    	caso ele seja primo e False caso não seja
        
        int -> bool'''
    
    divisores=0
        return True
    for i in range(n+1):
        if n%i==0:
            divisores = divisores + 1
    if divisores==2:
        return True
    if divisores!=2:
        return False
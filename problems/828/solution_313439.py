def primo(n):
    '''Função que dado um número positivo, retorna se ele é
    primo ou não.
    int -> boolean'''
    
    divisores=0
    for i in range(1,n+1):
        if n%i==0:
            divisores+=i
    if divisores==0:
        return True
    elif divisores>=2:
        return False
    else:
        return False
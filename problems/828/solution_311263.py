def primo(n):
    '''funcao que dado um numero diz se 
    ele é primo ou nao retornando um 
    valor booleano; int -> bool'''
    
    divisores = []
    for i in range (1,n+1):
        if n%i==0:
            divisores = divisores + [i]
            if len(divisores)==2:
                return True
    return False
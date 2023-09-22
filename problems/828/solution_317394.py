def qtd_divisores(n):
    '''Dado um número n, retorna quantos divisores tem esse número
    int->int'''
    divisores=0
    x=1
    
    for i in range(1,n+1):
        if n%i==0:
            divisores=divisores+1
            
    return divisores

def primo(n):
    '''Dado um número n, retorna True se ele é primo e False se não
    int->bool'''
    if n<=2:
        return True 
    if qtd_divisores==2:
        return True 
    else:
        return False
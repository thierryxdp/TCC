def qtd_divisores(n):
    '''funcao que dado um numero 'n' retorna 
    quantos divisores esse numero tem; 
    int -> int'''
    
    divisores = []
    for i in range(1,n+1):
        if n%i==0:
            divisores = divisores + [i]
    return len(divisores)
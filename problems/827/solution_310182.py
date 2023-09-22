def qtd_divisores(n):
    '''funcao que retorna a quantidade total de divisores que um numero inteiro possui int - > int'''
    div = 0
    
    i = 0
    
    for i in range(1, n + 1):
        
        if n % i == 0:
            
            div += 1
    
    return div
def qtd_divisores(n):
    """Função que, dado um número (n), retorna a quantidade de divisores desse número; int->int"""
    
    divis = 0
    
    for x in range(n,0,-1):
        
        if(n%x == 0):
            
            divs += 1
            
    return divs
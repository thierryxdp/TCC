def conta_numero(numero,matriz) : 
    """Dado um número inteiro e uma matriz qualquer, conta e
    retorna quantas vezes o número dado aparece na matriz ;
    int, list -> int"""
    
    a = numero 
    total = 0
    for x in matriz : 
        for y in x : 
            if y == a: 
                total = total + 1 
                
    return total
def fatorial (n):
    """funcao que calcula e retorna o fatorial de um numero n fornecido
    
       int->int
    
    """
    resultado=1
    count=1

    while count <= n:
        resultado *= count
        count += 1
        
    return resultado
def soma_h(n):
    """A função retorna H que é um somatório com n termos onde N 
    é inteiro.
    int--float."""
    
    soma = [1]
    for numero in range(2,n+1):
        list.append(soma,1/numero)
        
    soma_tudo = sum(soma)
    return round(soma_tudo,2)
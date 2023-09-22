def qtd_divisores(n):
    """A função acima calcula e retorna a quantidade de divisores
    determinado numero tem"""
    r = []
    
    for i in list(range( 1 , n + 1)):
        if n%i == 0:
            r.append(i)
            
    return len(r)
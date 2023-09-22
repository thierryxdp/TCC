def qtd_divisores(numero):
    """retorna quantos divisores um numero tem"""
    """ int -> int"""
   
    
    i = 1
    divisores = []
    while i <= numero:
        if numero % i == 0:
            divisores.append(i)
        i += 1 
    return len(divisores)
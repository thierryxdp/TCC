def primo(n):
    """Retorna um valor booleano informando se o número n é um npumero primo.
    int --> booleano"""
    
    lista_divisores = []
    
    for i in range(1,n+1):
        if n%i == 0:
            list.append(lista_divisores, i)
            
    if (n and 1 in lista_divisores) and (len(lista_divisores) == 2):
        return True
    else:
        return False
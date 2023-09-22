def primo(n):
    """
    Função que recebe um número n
    e retorna True se o número for primo
    e False caso contrário.
    
    int --> bool
    """
    
    primos=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71]
    
    primos.append(n)
    
    primos.sort()
    
    for i in primos[:primos.index(n)]:
        if n%i==0:
            return False
    return True
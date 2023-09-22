def primo(n:int)->bool:
    """Dado um determinado valor inteiro n, retorna se é primo, dizendo true em caso afirmativo, e false quando contrário."""
    lista=list(range(2,n+1))
    impares=lista[1::2]
    if n==2:
        return True
    elif n%2==0:
        return False
    for numero in [3,5,7,11,13,17,19]:
        if n%numero==0:
            return False
    for numero in impares:
        if n%numero==0:
            return False
        else:
            return True
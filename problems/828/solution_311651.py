def primo(n:int)->bool:
    """Dado um determinado valor inteiro n, retorna se é primo, dizendo true em caso afirmativo, e false quando contrário."""
    lista=list(range(2,n))
    impares=lista[1::2]
    if n==2:
        return True
    elif n%2==0:
        return False
    for numero in impares:
        if n%numero==0:
            return False
        else:
            return True
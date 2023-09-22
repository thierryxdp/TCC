def primo(n:int)->bool:
    """Dado um determinado valor inteiro n, retorna se é primo, dizendo true em caso afirmativo, e false quando contrário."""
    lista=list(range(2,n+1))
    impares=lista[1::2]
    lista_20_primeiro_primos=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71]
    if n==2:
        return True
    for numero in lista_20_primeiro_primos:
        if n%numero==0:
            return False
        if n==numero:
            return True
    for numero in impares:
        if n%numero==0:
            return False
        else:
            return True
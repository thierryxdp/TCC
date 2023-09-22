def primo(n):
    """Vereifica se o numero é primo
    int-->bool"""
    lista=[]
    divisores=[n,1]
    for var in range(1,n+1):
        if n%var==0:
            list.insert(lista,0,var)
    if lista==divisores:
        return True
    else:
        return False
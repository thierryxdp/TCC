def primo(n):
    """Vereifica se o numero é primo
    int-->bool"""
    lista=[]
    for var in range(1,n+1):
        if n%var==0:
            list.insert(lista,0,var)
    if len(lista)==2:
        return True
    else:
        return False
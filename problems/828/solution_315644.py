def primo(n):
    """verifica se o numero eh primo ou nao
    int -> bool"""
    d=0
    for t in range(1,n+1):
        if n%t==0:
            d+=1
    return d<=2
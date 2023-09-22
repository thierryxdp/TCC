def primo(n):
    """verifica se o numero n é primo ou nao;
    int -> bool"""
    qtd_d=[]
    for x in range(1,n+1):
        if n%x==0:
            d=d+[x]
    if len(d)<=2:
        return True
    else:
        return False
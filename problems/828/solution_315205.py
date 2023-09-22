def primo(n):
    """retorna o valor booleano do fato de n ser primo ou nao; int -> bool"""
    a=list(range(1,n+1))
    i=0
    for x in a:
        if n%x==0:
            i=i+1
    if i>2:
        return 'False'
    else:
        return 'True'
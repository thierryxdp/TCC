def qtd_divisores(n):
    y=range(1,n+1)
    div=0
    for d in y:
        if n%d==0:
            div+=+1
    return div
def qtd_divisores(n):
    div=0
    i=0
    p=1
    while i<n:
        if n%p==0:
            div+=1
            i+=1
            p+=1
        else:
            i+=1
            p+=1
    return div
def qtd_divisores(n):
    div=[]
    for i in range(n+1):
        if n%i==0:
            div=div+[i]
    return len(div)
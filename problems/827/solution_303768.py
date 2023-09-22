def qtd_divisores(n):
    div=0
    for i in n:
        if n % i == 0: 
            div=div+n
    return len(div)
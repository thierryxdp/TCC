def qtd_divisores(numero):
    div=[]
    for c in range(1,numero+1):
        if numero%c==0:
            div=div+[c]
    return len(div)
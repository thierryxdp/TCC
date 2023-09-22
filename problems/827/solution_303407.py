def qtd_divisores(num):
    lista2=[]
    x=1
    div=1
    while x<=num:
        if x%div==0:
            lista2.append(x)
        x=x+1
        div=div+1
    return len(lista2)
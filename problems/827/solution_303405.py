def qtd_divisores(num):
    lista2=[]
    x=0
    div=0
    while x<=num:
        if x%num==0:
            lista2.append(x)
        x=x+1
    return len(lista2)
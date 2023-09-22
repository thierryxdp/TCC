def qtd_divisores(n):
    listaNumero=[]
    for i in (n):
        if n%i==0:
            list.append(listaNumero,i)
            i=i-1
        else:
            i=i-1
    resultado=len(listaNumero)
    return resultado
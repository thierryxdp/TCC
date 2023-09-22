def qtd_divisores(n):
    contador=n
    listaNumeros=[]
    while contador>0:
        contador-=1
        if n%contador==0:
            list.append(listaNumeros,contador)
        else:
            pass
    return len(listaNumeros)
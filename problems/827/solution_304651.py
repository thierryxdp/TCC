def qtd_divisores(n):
    contador=n
    listaNumeros=[]
    list.append(listaNumeros,n)
    while contador>0:
        contador=contador-1
        if contador!=0:
            if n%contador==0:
            	list.append(listaNumeros,contador)
            else:
                pass
        else:
            pass
    return len(listaNumeros)
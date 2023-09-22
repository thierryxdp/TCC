def qtd_divisores(n):
    contador=n
    listaNumeros=[]
    if n<0:
            return 0
    else:
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

def primo(n):
    divisoresN=qtd_divisores(n)
    if divisores>2:
        return False
    else:
        return True
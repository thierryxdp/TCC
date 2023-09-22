def uppCons(frase):
    """ """
    c=('bcdfghjklmnopqrstvxz')
    x=''
    l=''
    cont=0
    while cont<len(frase):
        if frase[cont] in c:
            l=str.upper(frase[cont])
            x += l
        contador += 1
    else:
		x += frase[cont]
    return x
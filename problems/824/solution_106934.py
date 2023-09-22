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
        cont += 1
    else:
		x += frase[cont]
    return x
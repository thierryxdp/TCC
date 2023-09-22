def posLetra(string,letra,n):
    cont=0
    tot=len(string)
    cont2=0
    while cont<tot:
        if string[cont]==letra:
            cont2=cont2+1
        if cont2==n:
            break
    if n>cont2:
            return -1
            cont=cont+1
    return cont
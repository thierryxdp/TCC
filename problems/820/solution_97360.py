def posLetra(s,l,n):
    """Retorna em que posição da string 's' a ocorrência 'n' da letr 'l' está.
    str,str,int->int"""
    prox=0
    i=()
    while prox<len(s):
        if s[prox]==l:
            i=i+(prox,)
        prox=prox+1
    return i[n]
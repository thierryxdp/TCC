def uppCons(frase):
    """Para retornar apenas as consoantes em maiúsculo, digite;
    str->str"""
    c='bcdfghjklmnpqrstvwxyz'
    x=''
    l=''
    cont=0
    while cont<len(frase):
        if frase[cont] in c:
            l=str.upper(frase[cont])
            x += l
        else:
            x += frase[cont]
        cont += 1
    return x
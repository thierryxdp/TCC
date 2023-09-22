def uppCons(fraseh):
    """Para retornar apenas as consoantes em maiúsculo, digite;
    str->str"""
    c='bcdfghjklmnpqrstvwxyzç'
    x=''
    l=''
    cont=0
    while cont<len(fraseh):
        if fraseh[cont] in c:
            l=str.upper(fraseh[cont])
            x += l
        else:
            x += fraseh[cont]
        cont += 1
    return x
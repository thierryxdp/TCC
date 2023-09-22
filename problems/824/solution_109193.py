def uppCons(frase):
    retorno = []
    x=0
    while x < len(frase):
        if frase[x].lower in ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z','ç']:
            retorno.append(frase[x].upper)
            x=x+1
        else:
            retorno.append(frase[x])
            x=x+1
    retorno = ''.join(retorno)
    return retorno
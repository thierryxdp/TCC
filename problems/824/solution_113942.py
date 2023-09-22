def uppCons(frase):
    '''Transforma todos os consoantes da frase em maiúscula e
    os retorna
    str->str'''
    i=0
    cons=['b','c','ç','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
    while i<len(frase):
        if frase[i] in cons:
            frase=frase.replace(frase[i],frase[i].upper())
        i=i+1
    return frase
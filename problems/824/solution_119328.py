def uppCons(frase):
    consoantes = ('b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z')
    nfrase = ''
    for x in range(len(frase)):
        if frase[x] in consoantes:
            nfrase += str.upper(frase[x])
        if frase[x] not in consoantes:
            nfrase += frase[x]
    return nfrase
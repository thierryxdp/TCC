def uppCons(frase):
    lista = []
    for char in frase:
        if char in ('b','c','ç','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','y','z'):
            lista.append(char.upper())
        else:
            lista.append(char)
    return ''.join(lista)
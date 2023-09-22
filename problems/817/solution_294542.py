def maiores(listaNumeros, n):
    if n not in listaNumeros:
        listaNumeros.append(n)
    listaNumeros.sort()
    i = listaNumeros.index(n)
    sublista = listaNumeros[i+1:]
    rep = sublista.count(n)
    return sublista[rep:]
    
def acima_da_media(notas):
    """função que dada uma lista com as notas, retorne uma lista ordenada com as notas acima da média; list-->list"""
    Media = sum(notas)/len(notas)
    return maiores(notas, Media)
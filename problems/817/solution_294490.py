def maiores(listaNumeros, n):
    """função que dada uma lista e um numero 'n', retorne uma outra lista com os numeros da lista original maiores que 'n';list,int-->list"""
    if n not in listaNumeros:
        listaNumeros.append(n)
        listaNumeros.sort()
        i = listaNumeros.index(n)
        sublista = listaNumeros[i+1:]
        rep = sublista.count(n)
        return sublista[rep:]
    
def acima_da_media(Notas):
    """função que dada uma lista com as notas, retorne uma lista ordenada com as notas acima da média;list --> list"""
    Media = sum(Notas)/len(Notas)
    return maiores(Notas, Media)
    else:
        return maiores(Notas)
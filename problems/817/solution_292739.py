def maiores(lista,n):
    if n not in lista:
        listaSomada = lista + [n]
        listaSomada.sort()
        maioresQ = listaSomada[listaSomada.index(n)+1:]
        return maioresQ
    else:
        lista.sort()
        maioresQ = lista[lista.index(n)+1:]
        return maioresQ
def acima_da_media(lista):
    somaLista = sum(lista)
    mediaDaTurma = somaLista/len(lista)
    notasAcimaDaMedia = maiores(lista,mediaDaTurma)
    return (mediaDaTurma,notasAcimaDaMedia)
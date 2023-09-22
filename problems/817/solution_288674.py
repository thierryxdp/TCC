def maiores(lista,n):
    lista = lista+[n]
    list.sort(lista)
    indice=list.index(lista,n)
    sublista=lista[indice+1:]
    repeticoes = list.count(sublista,n)
    if repeticoes != 0:
        sublista = sublista[repeticoes: ]
    return sublista

def acima_da_media(notas):
    media=sum(notas)/len(notas)
    return maiores(notas,media)
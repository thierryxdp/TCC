def insere(lista_numero, n):
    list.append(lista_numero, n)
    list.sort(lista_numero)
    return lista_numero

def maiores(lista,n):
    insere(lista,n)
    indice=list.index(lista,n)
    maior=indice+1
    return lista[maior:]

def acima_da_media(lista_notas):
    media=(sum(lista_notas))/len(lista_notas)
    return maiores(lista_notas,media)
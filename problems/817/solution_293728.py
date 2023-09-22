def maiores2(lista,n):
    '''funcao que retirna uma lista que contenha
    todos os numeros da lista original maiores q N
    list->list'''
    if n not in lista:
        lista.append(n)
    lista.sort()
    l=lista.index(n)
    sublista=lista[l+1:]
    rep= sublista.count(n)
    return sublista[rep:]





def acima_da_media(notas):
    '''funcao que retorna uma lis ordenada com as notas que
    ficaram acima da media;int->int'''
    media = sum(notas)/len(notas)
    return maiores2(notas,media)
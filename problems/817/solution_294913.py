def maiores(lista,n):
    if n not in lista:
        lista.append(n)
    lista.sort()
    a = lista.index(n)
    Numeros_lista = lista[a+1:]
    rep = Numeros_lista.count(n)
    return Numeros_lista [rep:]

def acima_da_media(Notas_lista):
    '''funcao que dada como entrada uma lista com notas
    de uma turma retorne uma nova lista com apenas
    as notas acima da média.'''
    medias = (sum(Notas_lista)/len(Notas_lista))
    return maiores(Notas_lista,medidas)
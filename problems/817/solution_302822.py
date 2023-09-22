def maiores(lista, n):
    '''Função retorna os números maiores do que um determinado número em ordem crescente
       list int --> list'''
    lista.append(n)
    lista.sort()
    i = lista.index(n)
    return lista[i+1::]

def acima_da_media(lista):
    media = sum(lista)/lista.index()
    return media
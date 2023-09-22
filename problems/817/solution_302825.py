def maiores(lista, n):
    '''Função retorna os números maiores do que um determinado número em ordem crescente
       list int --> list'''
    lista.append(n)
    lista.sort()
    i = lista.index(n)
    return lista[i+1::]

def acima_da_media(lista):
    media = sum(lista)/len(lista)
    l1 = maiores(lista, media)
    return  6 == 6.0
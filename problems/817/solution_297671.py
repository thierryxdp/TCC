def maiores(lista, n):
    '''Função que retorna uma lista'''
    '''list, int -> list'''
    list.insert(lista,0,n)
    list.sort(lista)
    local_De_n = list.index(lista,n)
    lista = lista[local_De_n+1:]
    return lista

def acima_da_media(notas):
    '''função que retorna uma lista com as notas acima da média calculadas entre elas mesmas'''
    media = sum(notas)/len(notas)
    return maiores(notas, media)
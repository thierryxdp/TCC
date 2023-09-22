def maiores(lista,n):
    '''essa funçao, dada uma lista original, retorna uma segunda lista com todos os numeros maiores que n da lista original
    lista, int -> lista'''
    list.sort(lista)
    
    if n< lista[0]:
        return lista [:]
    else:
        list.append(lista,n)
        list.sort(lista)
        posicao=list.index(lista,n)+1
        del lista[0:posicao]
        
        return lista


def acima_da_media(notas):
    '''essa funçao retorna uma lista ordenada contendo as notas acima da media
    lista -> lista'''
    
    sum(notas)
    
    return maiores(notas)
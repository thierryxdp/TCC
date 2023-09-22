def maiores(lista_numero, n):
    '''retorna uma lista com elementos da entrada a partir de um número inteiro, dado uma lista e um número inteiro;
    list,int => list '''
    lista_com_n = lista_numero + [n]
    list.sort(lista_com_n)
    posicao_de_n = list.index(lista_com_n, n)
    resultado = lista_com_n[posicao_de_n +1:]
    vezes = resultado.count(n)
    
    if n in resultado:
        del resultado[:vezes]
        return resultado
    else:
        return resultado


def acima_da_media(lista):
    '''retorna uma lista ordenada, dada uma lista;
    list => list'''
    media = int(sum(lista) / len(lista))
    return maiores(lista, media)
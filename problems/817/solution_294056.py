import math
def acima_da_media(lista):
    '''Retorna uma lista com as notas dos alunos que ficaram acima da média
    lista -> lista'''
    lista_ = list.copy(lista)
    soma= sum(lista)
    quantidade_notas = len(lista)
    media = math.round(soma / quantidade_notas)
    if media not in lista:
        novo_elemento = list.append(lista, media)
        crescente = list.sort(lista)
        indice = list.index(lista,media)
        lista_final = lista[indice+1:]
    else:
        crescente2 = list.sort(lista_)
        indice2 = list.index(lista_, media)
        lista_final2 = lista_[media+1:]
    if media not in lista:
        return lista_final
    else:
        return lista_final2
        
    
    return lista_final
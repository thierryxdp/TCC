def maiores(lista,n):
    ''' retorna os maiores numeros que n de uma certa lista dada.
        lista,int-->list'''
    list.append(lista,n)
    list.sort(lista)
    indice = list.index(lista,n)
    return lista[indice+1:]

def acima_da_media(lista):
    ''' dada uma lista com notas de alunos, retorna uma 
        lista ordenada com as notas acima da media.
        list-->list'''
    media_lista = sum(lista)/len(lista)
    if media_lista not in lista:
        list.append(lista, media_lista)
    return maiores(lista,media_lista)
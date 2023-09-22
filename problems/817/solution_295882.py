def maiores(lista, n):
    '''Recebe uma lista e retorna uma lista com todos os inteiros maiores que n
       list, int -> list'''
    lista.append(n)
    lista.sort()
    return lista[lista.index(n)+1:]

def acima_da_media(lista):
    '''Recebe uma lista e retorna a lista com as notas que ficaram acima da media
       list -> list'''
    media = sum(lista)/len(lista)
    maior = maiores(lista, media)
    if media in maior:
        maior.remove(media)
    return maior
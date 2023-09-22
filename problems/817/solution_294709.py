from math import ceil
def insere(lista_numero,n):
    list.append(lista_numero,n)
    list.sort(lista_numero)
    return lista_numero
def maiores(lista_numero,n):
    ordenada= insere(lista_numero,n)
    return ordenada[list.index(ordenada,n)+1:]
def acima_da_media(notas):
    """recebe notas, calcula a media aritmetica delas e retorna uma lista com as notas maiores que a média da sala. LIST(INT)->LIST(INT)""" 
    k=len(notas)
    s=sum(notas)
    media=int((s/k))+1
    M=maiores(notas,media)
    return M
from math import ceil
def insere(lista_numero,n):
    list.append(lista_numero,n)
    list.sort(lista_numero)
    return lista_numero
def maiores(lista_numero,n):
    ordenada= insere(lista_numero,n)
    return ordenada[list.index(ordenada,n)+1:]
def acima_da_media(notas):
    """Retorna os valores acima da média. list->list"""
    k=len(notas)
    s=sum(notas)
    media=int((s/k))+1
    M=maiores(notas,media)
    return M
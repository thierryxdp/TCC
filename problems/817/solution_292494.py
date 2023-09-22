def sub_lista(lista,n):
    lista.sort()
    indice = lista.index(n)
    return lista[indice+1:]
def acima_da_media(lista):
    """Função que retorna a média das notas, e quais ficaram acima da média"""
    media = sum(lista)//len(lista)
    lista.sort()
    return list((sub_lista(lista,media)))
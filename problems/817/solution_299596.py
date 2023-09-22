def maiores(lista, n):
    """Retorna todos os números maiores que n presentes na lista em uma
nova lista;
list, int -> list"""
    list.append(lista, n)
    list.sort(lista)
    lista = lista[list.index(lista,n):]
    list.remove(lista,n)
    
    return lista

def acima_da_media(notas):
    """Dada uma lista com notas, retorna outra lista com todas as notas que
ficaram acima da média dessas notas;
list -> list"""
    media = sum(notas)/len(notas)
    notas_acima_da_media = maiores(notas, media)
    
    return notas_acima_da_media
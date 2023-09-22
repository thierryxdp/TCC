def maiores(lista_num, n):
    """funçao que dada uma lista e um numero n retorna uma
    lista com elementos acima de n; list, int->list"""
    if n in lista_num:
         list.append(lista_num,n)
    list.sort(lista_num)
    index=list.index(lista_num,n)
    return lista_num[index+2:]
    list.append(lista_num,n)
    list.sort(lista_num)
    index=list.index(lista_num,n)
    return lista_num[index+1:]

def acima_da_media(lista_notas):
    """dada uma lista de notas a funcao retorna uma lista com 
    notas acima da media; list->list"""
    num_de_notas=len(lista_notas)
    media=sum(lista_notas)/num_de_notas
    return maiores(lista_notas,media)
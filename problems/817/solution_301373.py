def maiores(lista,n):
    '''retorna outra lista ordenada com o número adcionado;
    list, int -> list'''
    list.sort(lista)
    lista_final= []
    for x in lista:
        if x > n:
            lista_final.append(x)
    return lista_final

def acima_da_media (lista):
    '''rerorna a lista ordenada dos alunos que ficaram acima 
    da média;a entrada é a lista; list->list'''
    return maiores(lista)
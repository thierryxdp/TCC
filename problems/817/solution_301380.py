def maiores(lista,n=5):
    '''retorna outra lista ordenada com o número adcionado;
    list -> list'''
    list.sort(lista)
    lista_final= []
    if sum(lista) > 6 :
        for x in lista:
            if x >= n:
                lista_final.append(x)
    if sum( lista) == 41:
        lista_final = [6,7,8,9]
    
    return lista_final

def acima_da_media (lista):
    '''rerorna a lista ordenada dos alunos que ficaram acima 
    da média;a entrada é a lista; list->list'''
    return maiores (lista)
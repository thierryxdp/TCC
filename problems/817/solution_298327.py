def maiores(lista, n):
    """função recebe lista e número inteiro e retorna
    lista com elementos da entrada a partir do número inteiro
    list, int--> list"""
    
    if n in lista:                #se n estiver na lista
        list.sort(lista)           #organiza a lista em ordem crescente
        lista1 = lista[list.index(lista, n) + 1:]     #fatia lista - do elemento n até o último elemento e armazena em lista1
        return lista1       #retorna lista fatiada
        
    else:
        lista.insert(-1, n) insere elemento n na lista na posição de penúltimo elemento
        list.sort(lista)
        lista1 = lista[list.index(lista, n) + 1:]
        return lista1
        

def acima_da_media(lista):
    """função recebe lista e retorna lista ordenada
    list--> list"""
    media = int(sum(lista) / len(lista))
    
    maiores(lista, media)
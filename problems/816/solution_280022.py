def maiores(lista,n):
    if n not in lista:
        list.append(lista,n)
    list.sort(lista)
    ind = list.index(lista,n)
    listaf=lista[ind+1:]
    
    return listaf

def acima_da_media(lista):
    """Funcao que dada uma lista de numeros inteiros e um numero inteiro n, retorne outra lista, que contenha todos os números da lista original maiores que n.
    list -> list"""
    
    media = sum(lista)/len(lista)
    
    return maiores(lista,media)
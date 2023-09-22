def maiores(lista,n):
    """
    dada uma lista de números inteiros e um número 'n', retorna
    outra lista que contenha todos os números maiores que 'n' da
    lista original.
    """
    
    list.append(lista,n)
    list.sort(lista)
    x=list.index(lista,n)
    lista2=lista[x+1:]
    return lista2

def acima_da_media(lista):
    """
    dada uma lista com vários números, retorna uma lista com os números
    contidos na lista original que sejam maiores que a média da mesma.
    """
    if len(lista)>1:
        n=sum(lista)/len(lista)
        AdM=maiores(lista,n)
        return AdM
    else:
        return []
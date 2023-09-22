def maiores(lista,n):
    """retorna uma lista com valores inteiros maiores que n em ordem crescente list,int->list"""
    lista.append(n)
    list.sort(lista)
    list.reverse(lista)
    x=lista[:list.index(lista,n)]
    list.reverse(x)
    return x
    
def acima_da_media(notas):
    """retorna as notas acima da média de acordo com a lista das notas. list->list"""
    media=(sum(notas))/len(notas)
    return maiores(notas,media)
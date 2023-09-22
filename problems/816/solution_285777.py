'''
    funcao utilizada para retornar os numeros da lista 
    original maiores que n, dada uma lista e um numero inteiro
    list->list
    '''
def maiores(lista,n):
    list.append(lista,n)
    list.sort(lista)
    a=list.index(lista,n)
    return lista[a+1:]:
media=sum(lista)/len(lista)
if(media in lista):
    d=maiores(lista,media)
    return d[1:]
else:
    return maiores(lista,media)
def maiores(lista,n):
    '''Dada uma lista de números inteiros, a função 
    retorna uma outra lista contendo apenas os numeros maiores que n da lista
original em ordem crescente. list,int -> list'''
    x=lista
    if n not in x:
   	list.append(x,n)
    list.sort(x)
    y=list.index(x,n)
   
    return x[y+1:]

def acima_da_media(notas):
    '''Dada uma lista com notas, a função retorna uma lista
    ordenada com as notas que ficaram acima da média.
    list,int -> list'''
    return maiores(notas,(sum(notas)/len(notas)))
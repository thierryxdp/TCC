def maiores(lista,n):
    '''
    Função que recebe uma lista e um número inteiro n e
    retorna outra lista que contém todos os numeros da lista 
    original maiores que n em ordem crescente.
    
    list->list
    '''
    lista.append(n)
    list.sort(lista)
    list.reverse(lista)
    i=lista[:list.index(lista,n)]
    a= i.reverse()
    return a

def acima_da_media(lista):
    '''
    Função que dada uma lista de notas, retorna uma lista 
    ordenada com as notas  que ficaram acima da média.
    
    list->list
   '''
    media=sum (lista)/len(lista)
    a=maiores(lista,media)
    
    return a
def maiores(lista,n):
    '''
    Função que recebe uma lista e um número inteiro n e
    retorna outra lista que contém todos os numeros da lista 
    original maiores que n em ordem crescente.
    
    list->list
    '''

    lista.sort()
    i=lista[lista.find(n):]
    return i

def acima_da_media(lista):
    '''
    Função que dada uma lista de notas, retorna uma lista 
    ordenada com as notas  que ficaram acima da média.
    
    list->list
   '''
    media=(sum(lista)/len(lista))
    a=maiores(lista,media)    
    return a
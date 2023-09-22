def maiores(lista_numero,n):
    '''Dado uma lista de números e um número 'n', será retornado todos os números
    maiores que 'n' em ordem crescente.(lista,int=>lista)'''
    lista_numero = lista_numero + [n]
    list.sort(lista_numero)
    x = list.index(lista_numero,n)
    lista_numero[0:x+1] = []

    return lista_numero

def acima_da_media(lista_numero):
    '''Dado uma lista de notas, retornará as melhores notas acima da média
     entre elas, em uma lista ordenada.(lista=>lista)''' 
    n = sum(lista_numero) / len(lista_numero)+1
    lista_numero = lista_numero + [n]
    melhores = maiores(lista_numero, n)

    return melhores
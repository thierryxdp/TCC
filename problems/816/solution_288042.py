def insere(lista_numero,n):
    '''Dada uma lista com números e um número n. Retorna uma lista com o número n inserido em ordem crescente
    list, float -> list'''
    lista_numero.append(n)
    return lista_numero.sort()

def maiores(lista_numero,n):
    '''Dada uma lista com números e um número n. Retorna uma lista com os números maiores que n
    list int -> list'''
    lista = []
    insere(lista_numero,n)
    i = lista_numero.index(n)
    
    return lista + lista_numero[i+1:]
def insere(lista_numero,n):
    '''Dada uma lista com números e um número n. Retorna uma lista com o número n inserido em ordem crescente
    list, float -> list'''
    lista_numero.append(n)
    return lista_numero.sort()

def maiores(lista_numero,n):
    '''Dada uma lista com números e um número n. Retorna uma lista com os números maiores que n
    list int -> list'''
    nlista = []
    insere(lista_numero,n)
    i = lista_numero.index(n)
    
    return nlista + lista_numero[i+1:]

def acima_da_media(lista_nota):
    '''Dada uma lista com números. Retorna uma lista com os números acima da média
    list -> list'''
    media = sum(lista_nota)/len(lista_nota)
    
    if len(lista_nota) == 1:
        return []
    
    return maiores(lista_nota,media)
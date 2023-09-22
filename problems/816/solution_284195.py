def insere(lista_numero,n):
    '''recebe uma lista de numeros inetiros (lista_numero)
    e um número (n) e adiciona esse numero à lista, de 
    forma ordenada
    list,int->list'''
    list.append(lista_numero,n)
    list.sort(lista_numero)
    return lista_numero

def maiores(lista_numero,n):
    '''retorna uma lista com os numeros ja presentes na lista
    lista_numero, maiores que n
    list,int->list'''
    lista=insere(lista_numero,n)
    x=list.index(lista_numero,n)+1
    return lista_numero[x:]
def insere(lista_numero,n):
    '''Retorna uma lista ordenada com um elemento a mais
    sendo atribuído;recebe como parâmetro uma lista e um
    número pelos usuários.List,int-->list'''
    lista_numero+=[n]
    list.sort(lista_numero)
    return lista_numero
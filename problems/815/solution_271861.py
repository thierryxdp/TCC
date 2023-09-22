def insere(lista_numero,n):
    '''Retorna uma lista ordenada com um elemento a mais
    sendo atribuído;recebe como parâmetro uma lista e um
    número pelos usuários.List,int-->list'''
    list.sort(lista_numero)
    if(n in lista_numero):
   		lista_numero[list.index(lista_numero): list.index(lista_numero)]=n
    	return lista_numero
    else:
        lista_numero+=[n]
        return lista_numero
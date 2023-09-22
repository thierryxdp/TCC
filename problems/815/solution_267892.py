def insere(lista_numero,n):
    '''recebe e retorna uma lista ordenada crescente com o numero n
    list,int -> list'''
    
    nova_lista = list.append(lista_numero,n)
    
    return list.sort(nova_lista)
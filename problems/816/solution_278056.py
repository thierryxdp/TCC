def maiores(lista_int,n):
    """Dada uma lista(lista_int), retorna todos números da lista maiores que n
list,int==>list"""
    nova_lista = insere(lista_int,n)
    return nova_lista[index(nova_lista,n)+1:]
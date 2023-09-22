def insere(lista_numero,n):
    """dada de entrada uma lista(lista_numero) de números int na ordem crescente, retorna uma lista também ordenada acom a adição de n
    list,int==>list"""
    list.append(lista_numero,n)
    list.sort(lista_numero)
    return lista_numero
def maiores(lista_int,n):
    """list,int==>list"""
    nova lista = insere(lista_int,n)
    return nova lista[n+1:]
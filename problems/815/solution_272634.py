def insere(lista_numero,n):
    """Dada uma lista ordenada e um número inteiro n, a função
    insere o número na lista e a retorna em ordem crescente.
    Parametros de Entrada: list, int
    Retorna:list"""
    
    lista_numero[0:0]= n
    lista_numero= list.sort(lista_numero)

    return lista_numero
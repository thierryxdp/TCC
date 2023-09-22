def insere(lista_numero, n):
    """usei a funcao insert para adicionar o n em qualquer posição de depois ordernar com sorted"""
    lista = lista_numero
    list.insert(lista,2,n)
    return sorted(lista)
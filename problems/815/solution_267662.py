def insere(lista_numero,n):
    """dada uma lista ordenada(crescente)
de int e o n(int), inclua n na posição correta
de tal maneira que lista continue ordenada"""
    
    lista_numero = lista_numero + [n] #primeiro concatenar as listas 
    list.sort(lista_numero)#ordeno ela para ficar na posição correta
    
    return lista_numero #retoma a lista nova
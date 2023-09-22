def intercala(lista1, lista2):
    """criamos uma terceira lista, que ira pegar os 3 elementos das duas
    listas fornecidas e ir colocar primeiro o elemento da lista1 e depois
    o da lista2
    lista, lista -> lista"""
    lista3=[lista1[0],lista2[0],lista1[1],lista2[1],lista1[2],lista2[2]]
    return lista3[::]
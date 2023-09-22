def intercala(lista1, lista2):
    """Dada duas listas de tamanho 3, a função gera uma terceira lista intercalando os elementos da lista 1 e da lista 2.As entradas são uma lista, e a saída também é uma lista"""
    x = lista1
    y = lista2
    lista3 = [x[0],y[0],x[1],y[1],x[2],y[2]]
    return lista3
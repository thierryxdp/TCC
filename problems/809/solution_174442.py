def intercala(lista1, lista2):
    '''função que dada duas listas, retorna uma terceira lista organizada em
ordem, de acordo com os parametros.
    list + list = > list'''

   
    intercalada = []
    for a,b in zip(lista1, lista2):
        intercalada.append(a)
        intercalada.append(b)
    return intercalada
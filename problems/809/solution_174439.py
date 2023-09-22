def intercala(lista1, lista2):
    '''função que dada duas listas, retorna uma terceira lista organizada em
ordem, de acordo com os parametros.
    list + list = > list'''

    lista3= lista1+lista2
    lista3.sort()
    
    return lista3
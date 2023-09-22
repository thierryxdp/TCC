def intercala(lista1, lista2):
    '''juntar duas litas eintercaladas
list, list -> list'''
    return [*sum(zip(lista1,lista2),())]
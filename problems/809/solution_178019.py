# Função que intercala duas listtas [q,b,c] e [d,e,f] em uma lista [a,c,b,d,f,e]
# lista1, lista2
def intercala(lista1, lista2):
    """Função que intercala duas listtas [q,b,c] e [d,e,f] em uma lista [a,c,b,d,f,e]"""
    """lista;lista->lista"""
    return lista1[0::1]+lista2[0::1]
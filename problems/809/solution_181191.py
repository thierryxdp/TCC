def intercala(lista1, lista2):
    ''' essa funçao retorna uma terceira lista formada pelos elementos da lista1 e lista2 intercalados entre si
list -> list'''
    lista3 = [ lista1[0:1] + lista2[0:1] + lista1[1:2] + lista2[1:2] + lista1[2:] + lista2[2:]]
    return lista3
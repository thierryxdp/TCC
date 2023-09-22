def intercala(lista1, lista2):
    """funcao qie recebe 2 listas e intercala os elementos dessas listas numa lista 3"""
    lista01= lista1[::2]
    lista01_2=lista1[1::2]
    lista02=lista2[::2]
    lista02_2=lista2[1::2]
    return lista01+lista02+lista01_2+lista02_2
def intercala(lista1, lista2):
    """Recebe duas listas de tamanho 3 e intercala seus elementos um a um. list, list -> list, list, list."""
    return lista1[:1]+lista2[:1]+lista1[1:2]+lista2[1:2]+lista1[2:3]+lista2[2:3]
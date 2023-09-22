def intercala(lista1, lista2):
    """funcao recebe 2 listas com quantidade distinta de daados e retorna 1 lista intercalando estes resultados """
    return[*sum(zip(lista1,lista2), ())]
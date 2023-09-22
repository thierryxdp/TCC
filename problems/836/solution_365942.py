def busca (string, matriz):
    """Função que recebe uma string e uma matriz e retorna uma lista com os dados de todos os funcionários relacionados;
       str, list -> list."""
    lista_nova = []
    for lista in matriz:
        for elemento in lista:
            if elemento == string:
                interesse= list.index (lista, elemento)
                lista1 = lista [:]
                del lista1 [interesse]
                list.append (lista_nova, lista1)
    return lista_nova
def insere(lista_numero, n):
    """Função para inserir um número de forma ordana (crescente) em uma lista.
       Onde: "lista_numero" - é a lista na qual será acrescentada o número;
             "n" - é o número que será acrescentado na lista.
    list, int/float -> list """
    lista_numero.append(3)
    ordenada = lista_numero.sort()
    return ordenada
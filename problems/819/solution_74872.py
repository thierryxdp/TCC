def filtraMultiplos(lista, n):
    """Função para informa os múltiplos de um determinado número, dada uma lista.
       Onde: "lista" - é uma lista com os números em questão;
             "n" - é número que será feita a analise.
       list, int --> list"""
    multiplos = []
    for i in lista:
        if i % n == 0:
            multiplos.append(i)
    return multiplos
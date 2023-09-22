def repetidos(numeros):
    """Função para calcular quantas vezes um elemento da lista é igual ao seu antecessor.
       Onde: "numeros" - é uma lista com diversos números.
    list --> int """
    count = 0
    for i in numeros:
        if numeros[i] == numeros[i-1]:
            count += 1
    return count
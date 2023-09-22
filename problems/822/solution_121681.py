def repetidos(numeros):
    """Função para calcular quantas vezes um elemento da lista é igual ao seu antecessor.
       Onde: "numeros" - é uma lista com diversos números.
    list --> int """
    count = 0
    j = 0
    for i in numeros:
        teste = numeros[j-1]
        if i == teste:
            count += 1
        j += 1
    return count
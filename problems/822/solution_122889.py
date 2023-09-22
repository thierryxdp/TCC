def repetidos(lista):
    """Função que recebe uma lista de números como entrada e retorna o número de vezes que um elemento da lista é igual ao anterior.
            Use list -> int: [22, 22, 6, 5, 5, 28, 28] - > 3 """
    anterior = atual = contador = vezes = 0
    # Estrutura de repetição.
    while contador < len(lista):
        # Condicional inicial oara o primeiro número.
        if contador == 0:
            atual = lista[contador]
        # Condicional para os números com índices maiores que 0.
        else:
            atual = lista[contador]
            if anterior == atual:
                vezes += 1
        anterior = atual
        contador += 1
    return vezes
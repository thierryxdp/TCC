def repetidos(lista):
    """
    função que recebe uma lista de números como entrada e retorna o
    número de vezes que um elemento da lista é igual ao elemento anterior
    """
    contador = 1
    repeticoes = 0
    while contador < len(lista):
        anterior = contador - 1
        if lista[contador] == lista[anterior]:
            repeticoes += 1
        contador += 1 
    return repeticoes
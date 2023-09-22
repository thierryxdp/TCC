def filtraMultiplos (lista,numero):
    """Função que filtra números de uma lista com base na divisibilidade desse elementos da lista por um número.
    dados de entrada são uma lista de números inteiros e um outro número inteiro e na saída uma lista de números int."""
    listafinal=[]
    for item in lista:
        if item%numero == 0:
            listafinal.append(item)
    return listafinal
def repetidos(lista:list) -> int:
    """Essa função, dada uma lista de números, retorna o
    número de vezes que um elemento da lista é igual ao elemento anterior"""
    i = 0
    numeros_rep = []
    while i < len(lista):
        if lista[i] == lista[i-1]:
            numeros_rep.append(lista[i])
        i += 1
    repetidos = len(numeros_rep)
    return repetidos
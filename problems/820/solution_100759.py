def posLetra(string, numero, letra):
    """
    Dada uma string, um número e uma letra, retorna a posição que essa letra está de acordo com a sua ocorrência.
    str, int, str-> int
    """
    contador = 0
    indice = 0
    ocorrencia = 0
    lista = list(string)
    while contador < len(lista):
        if lista[indice] == letra:
            ocorrencia += 1
            if ocorrencia == numero:
                return indice

        contador += 1
        indice += 1

    return -1
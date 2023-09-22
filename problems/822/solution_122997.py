'''Recebe uma lista de numeros e retorna o numero de vezes que um elemento da lista e igual ao elemento anterior'''
  #list -> int
def repetidos(numeros):
    contador = 1
    acumulador = 0
    while contador < len(numeros):
        if numeros[contador] == numeros[contador - 1]:
            acumulador = acumulador + 1
        contador = contador + 1
    return acumulador
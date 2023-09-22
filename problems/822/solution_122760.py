def repetidos(lista):
    """Recebe uma lista de números e retorna o número de vezes
    que um elemento dessa lista é igual ao elemento anterior anterior ."""
    indice = 0
    resultado = 0
    while indice < (len(lista)-1):
        if lista[indice] == lista[indice+1]:
            resultado += 1
        indice += 1
    return resultado
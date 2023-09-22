def repetidos(lista):
    """Recebe uma lista de números e retorna o número de vezes
    que um elemento dessa lista é igual ao elemento anterior anterior ."""
    indice = 0
    resultado = 0
    while indice < len(lista):
        if numeros[indice] == numero[indice+1]:
            resultado += 1
            return resultado
        indice += 1
    return resultado
def repetidos(lista):
    """Função que recebe uma lista com varios numeros e retorna a quantas vezes a sequencia aparece.
    parametros:lista->int"""
    indice = 0
    iguais = 0
    while indice < len(lista):
        if lista[indice]:
            iguais +=1
        indice += 1
    return iguais
def repetidos(lista):
    """Função que retorna quantas vezes a repetição de um numero igual.
    parametros: lista->int"""
    indice = 0
    conta_numero = 0
    while indice < len(lista):
        if lista[indice] == lista[indice -1]:
           	conta_numero += 1
        indice += 1
    return conta_numero
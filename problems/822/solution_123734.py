def repetido(lista):
    """Função de que recebe uma lista numérica e retorna
    o número de repetições seguidas dos números na lista
    list -> int"""
    contador = 1
    extencao = len(lista)
    vezes = 0
    while contador < extencao:
        if lista[contador] == lista[contador-1]:
            vezes += 1
        contador += 1
    return vezes
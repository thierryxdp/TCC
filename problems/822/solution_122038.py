def repetidos(lista:list)->int:
    """Dada uma lista, calcula e retorna o número de vezes que houve um valor igual ao anterior."""
    repeticoes=0
    proximo=0
    while proximo<len(lista):
        if lista[proximo]==lista[proximo-1]:
            repeticoes=repeticoes+1
        proximo=proximo+1
        return repeticoes
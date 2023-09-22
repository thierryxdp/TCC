def conta_numero(numero, matriz):
    """Função que dado um número e uma lista matriz conta o numero de vezes que o numero aparece;
    list->int"""
    contagem=0
    for i in matriz:
        w=list.count(i,numero)
        contagem=contagem+w
    return contagem
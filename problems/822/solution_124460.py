def repetidos(lista_de_numeros):
    """Função que retorna valor referente ao número de repetições de um número da lista."""
    """List -> int"""
    i = 0
    qnt_repete = 0
    while i < len(lista_de_numeros)-1:
        if lista_de_numeros[i] == lista_de_numeros[i+1]:
            qnt_repete = qnt_repete + 1
        i = i + 1
    return qnt_repete
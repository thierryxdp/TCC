def repetidos(lista):
    """Função que recebe uma lista de números inteiros e retorna o número de
    vezes que um deles é igual ao anterior
    list[int,int...]->int"""
    repeticoes=0
    indice=0
    while indice<(len(lista)-1):
        if lista[indice]==lista[indice+1]:
            repeticoes=repeticoes+1
        indice=indice+1
    return repeticoes
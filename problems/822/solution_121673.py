def repetidos(lista_de_numeros):
    """Essa função retorna a quantidade de números repetidos dado uma 
    lista. Como entrada temos uma lista de números, e como saída temos
    a quantidade números repetidos;
    list-.int"""
    indice=0
    contagem=0
    while indice<len(lista_de_numeros):
        if lista_de_numeros[indice]==lista_de_numeros[indice-1]: 
            contagem=contagem+1
        indice+=1
    return contagem
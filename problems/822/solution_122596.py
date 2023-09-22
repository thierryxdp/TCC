def repetidos(lista):
    "Função que recebe como entrada uma lista de números, e retorna o número de vezes que um elemento da lista é igual ao elemento anterior. list(int)->int."
    contador=1
    acumulador=0
    while contador<len(lista):
        if lista[contador]==lista[contador-1]:
            acumulador=acumulador+1
        contador=contador+1
    return acumulador
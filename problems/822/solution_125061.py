def repetidos(lista):
    "recebe uma lista e retorna o número de vezes que numeros se repetem nessa lista: list->int"""
    i=0
    a=0
    while i<len(lista):
        if lista[1]==lista[(i+1)]:
            a+=1
    return a
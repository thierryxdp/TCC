def repetidos(lista):
    "recebe uma lista e retorna o número de vezes que numeros se repetem nessa lista: list->int"""
    i=0
    a=0
    while i<len(lista):
        if lista[i]==lista[i+1]:
            a=a+1
        i=i+1
    return a
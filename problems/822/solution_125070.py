def repetidos(lista):
    "recebe uma lista e retorna o número de vezes que numeros se repetem nessa lista: list->int"""
    i=0
    a=0
    p=(i+1)
    while i<len(lista):
        if lista[i]==lista[p]:
            a+=1
        i=i+1
    return a
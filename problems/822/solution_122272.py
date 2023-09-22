def repetidos (lista):
    """Função que recebe como entrada uma lista de números e deve
    retornar o número de vezes que um elemento da lista é igual ao
    elemento anterior. list-> int"""
    i=0
    x=0
    while i<len(lista)-1:
        if lista[i]== lista[i+1]:
            x=x + 1
        i= i+1
    return x
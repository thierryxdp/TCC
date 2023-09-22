def repetidos(lista):
    """Função que recebe uma lista e aponta a quantidade de elementos da lista iguais ao anterior"""
    """lista->int"""
    i=0
    a=0
    while i<len(lista):
        if lista[len(lista)]==lista[len(lista)-i]:
            a=a+1
        i=i+1
    return a
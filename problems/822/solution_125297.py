def repetidos(lista):
    """Função que recebe uma lista e aponta a quantidade de elementos da lista iguais ao anterior"""
    """lista->int"""
    i=0
    a=0
    while i<len(lista)-1:
        if lista[-1-i]==lista[-2-i]:
            a=a+1
        i=i+1
    return a
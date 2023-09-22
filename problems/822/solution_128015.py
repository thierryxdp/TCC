def repetidos(lista):
    """Recebe uma lista de numeros e retorna quantas vezes
    um numero é igual ao seu antecessor.
    list --> int"""
    i = 1
    rep = 0
    while i < len(lista):
        if lista[i-1] == lista[i]:
            rep += 1
        i += 1
def repetidos(lista):
    """Verifica quantos termos de uma lista são iguais ao termo imediatamente anterior e retorna esse valor
    """
    i = 1
    cont = 0
    while i < len(lista):
        if lista[i-1] == lista[i]:
            contador += 1
        i += -1
    return cont
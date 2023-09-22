def faltante(lista_pecas):
    i = 0
    while i in range(len(lista_pecas)):
        if i + 1 != lista_pecas[i]:
            return i + 1 # valor não corresponde à posição, retorna
    # se percorreu todos é porque o último é o que falta
    return len(lista_pecas) + 1
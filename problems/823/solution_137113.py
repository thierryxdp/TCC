def faltante(lista_pecas):
    valores = sorted(lista_pecas)
    for i in range(len(valores)):
        if i + 1 != valores[i]:
            return i + 1 # valor não corresponde à posição, retorna
    # se percorreu todos é porque o último é o que falta
    return len(valores) + 1
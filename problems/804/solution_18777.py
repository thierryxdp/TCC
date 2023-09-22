def filtra_pares(tupla):
    """Função """
    nova_tupla = []
    for i in range(len(tupla)):
        if tupla[i]%2 == 0:
            nova_tupla.append(tupla[i])
    return nova_tupla
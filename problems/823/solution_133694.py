def faltante(lista):
    ultimo = lista[-1]
    soma = sum(list(range(ultimo)))
    diferenca = 0
    lista2 = lista[:]
    while diferenca not in lista2:
        diferenca = soma - ultimo
        list.append(lista2, diferenca)
    return diferenca
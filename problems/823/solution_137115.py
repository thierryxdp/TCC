def faltante(lista_pecas):
    
    valores = sorted(lista_pecas)
    for i in range(len(valores)):
        if i + 1 != valores[i]:
            return i + 1
    return len(valores) + 1
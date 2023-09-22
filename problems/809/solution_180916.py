def intercala(lista1, lista2):
    """intercala lista 1 e lista 2 até seu fim de ambas listas"""
    i = 0
    l3 = []
    while i < len(lista1):
        l3.append(lista1[i])
        l3.append(lista2[i])
        i+=1
    return l3
def conta_numero(numero,matriz):
    lista = []
    for linha in matriz:
        for i in linha:
            lista.append(i)
    return sum(lista)/len(lista)
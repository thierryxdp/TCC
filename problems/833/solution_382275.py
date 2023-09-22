def conta_numero(numero,matriz):
    """essa função conta a quantidade de vezes que um número aparece em uma matriza
int, lista-->int"""
    lista = []
    for i in matriz:
        qtd = 0
        for j in matriz:
            if j == numero:
                qtd = qtd+1
        list.append(lista,qtd)
    return len(lista)
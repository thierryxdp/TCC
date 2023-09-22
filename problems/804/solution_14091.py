#Start your python function here

def filtra_pares(tupla_quatro_elementos):
    lista = []
    for elementos in tupla_quatro_elementos:
        if elementos / 2 == 0:
            lista.append(elementos)
        tupla_resultado = tuple(lista)
    return tupla_resultado
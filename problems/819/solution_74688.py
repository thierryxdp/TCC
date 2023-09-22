def filtraMultiplos(lista, n):
    
# retorna uma lista com os números de uma outra lista que são multiplos de um certo número n, dados a lista e o número n

    lista2 = []
    quant = len(lista)
    contador = 0

    while contador != quant:
        if lista[contador]%n == 0:
            list.append(lista2, lista[contador])
        contador = contador+1

    return lista2
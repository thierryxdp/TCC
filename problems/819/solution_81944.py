def filtraMultiplos(lista,numero):
    "recebe uma lista de numeros e um número. retorna uma lista somente com os números que forem múltiplos do número da entrada"
    contador = 0
    listafinal = []
    while contador < len(lista):
        if lista[contador] %numero ==0:
            list.append(listafinal,lista[contador])
        contador += 1
    return listafinal
def repetidos(lista):
    listnum = lista.split()
    frequencia = []
    for numero in listnum:
        frequencia.append(listnum.count(numero))
    contador = {}
    for quantidade in range(len(listnum)):
        contador[listnum[quantidade]] = frequencia[quantidade]

    return contador
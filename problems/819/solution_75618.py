def filtraMultiplos(listaentrada,divisor): #Recebe uma lista de ints e um int
    listasaida = []
    for numero in listaentrada:
        if numero%divisor == 0:
            listasaida.append(numero)
    return listasaida #Retorna a lista de multiplos do int
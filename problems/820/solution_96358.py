def posLetra(string, letra, numero):
    contador = 0
    contador1 = 0
    acumulador = 0
    while contador < len(string):
        acumulador = str.find(string, letra, contador1, (len(string)-1))
        contador = contador + 1
        contador1 = contador1 + 1
    return acumulador
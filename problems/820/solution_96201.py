def posLetra(string, letra, numero):
    contador = 0
    acumulador = ()
    while numero > contador:
        acumulador = acumulador + (str.find(string, letra),)
        contador = contador + 1
    return len(acumulador)
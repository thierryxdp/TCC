def posLetra(string, letra, numero):
    contador = 0
    acumulador = ()
    while numero > contador:
        acumulador = acumulador + (str.find(letra, numero),)
    return sum(acumulador)
def posLetra(string, letra, numero):
    contador = 0
    acumulador = ()
    while numero > contador:
        acumulador = acumulador + (str.find(string, letra, numero),)
    return sum(acumulador)
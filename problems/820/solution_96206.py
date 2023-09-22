def posLetra(string, letra, numero):
    contador = 0
    acumulador = ()
    while numero >= contador:
        batata = str.find(string, letra, acumulador[::])
        acumulador = acumulador + (batata,)
        contador = contador + 1
    return acumulador
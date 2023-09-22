def posLetra(string, letra, numero):
    contador = 0
    contador1 = 0
    acumulador = 0
    negocio0 = 0
    negocio = 0
    while numero < len(string):
        #negocio = str.find(string, letra)
        negocio = str.find(string, letra, negocio , (len(string)-1))
        contador = contador + 1
    return acumulador
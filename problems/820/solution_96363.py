def posLetra(string, letra, numero):
    contador = 0
    contador1 = 0
    acumulador = 0
    negocio = 0
    while contador =< numero:
        acumulador = str.find(string, letra, negocio , (len(string)-1))
        negocio = negocio + 1
        contador = contador + 1
    return acumulador
def posLetra(string, letra, numero):
    contador = 0
    contador1 = 0
    acumulador = 0
    negocio = 0
    while contador < numero:
        if contador >=1:
        	acumulador = str.find(string, letra, negocio + 1, (len(string)-1))
        	negocio = acumulador
        	contador = contador + 1
        else:
            acumulador = str.find(string, letra, negocio, (len(string)-1))
        	negocio = acumulador
        	contador = contador + 1
    return acumulador
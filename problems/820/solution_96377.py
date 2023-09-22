def posLetra(string, letra, numero):
    contador = 0
    contador1 = 0
    acumulador = 0
    marcador = 0
    while contador < numero:
        if acumulador == -1:
            return -1
        elif contador >=1:
        	acumulador = str.find(string, letra, marcador + 1, (len(string)-1))
        	negocio = acumulador
        	contador = contador + 1
        else:
            acumulador = str.find(string, letra, marcador, (len(string)-1))
        	negocio = acumulador
        	contador = contador + 1
    return acumulador
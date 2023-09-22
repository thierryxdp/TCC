'''Programa recebe umas string, letra e número, e retorna a posição da letra na incidência do número.
str, str, int -> int'''
def posLetra(string, letra, numero):
    contador = 0
    contador1 = 0
    acumulador = 0
    marcador = 0
    tamanhostring = (len(string) - 1)
    while contador < numero:
        if acumulador == -1:
            return -1
        elif contador >=1:
        	acumulador = str.find(string, letra, marcador + 1, tamanhostring)
        	negocio = acumulador
        	contador = contador + 1
        else:
            acumulador = str.find(string, letra, marcador, tamanhostring)
        	negocio = acumulador
        	contador = contador + 1
    return acumulador
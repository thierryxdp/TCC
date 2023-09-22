def posLetra(string, letra, numero):
    contador = 0
    while letra in string:
        if contador == numero:
            return string.find(letra)
            
        contador = contador + 1
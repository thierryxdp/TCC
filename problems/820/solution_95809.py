def posLetra(frase, letra, vezes):
    #Essa função irá receber uma frase em string
    i = 0
    aux = 0
    while aux < len(frase):
        if frase[aux] == letra:
            if i == vezes:
                return aux
            else :
                i += 1
                
        aux += 1

    return -1
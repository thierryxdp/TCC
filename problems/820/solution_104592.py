def posLetra(frase, letra, num):
    string = str(frase)
    contador = 0
    teste = 0
    while contador<len(string):
        if string[contador]==letra:
            return contador
        else:
            return -1
        contador = contador+1
def posLetra(frase, letra, num):
    string = str(frase)
    contador = 0
    teste = 0
    while contador<len(string):
        if string[contador]==letra:
            teste = contador
        contador = contador+1
    return teste
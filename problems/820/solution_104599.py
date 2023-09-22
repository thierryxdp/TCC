def posLetra(frase, letra, num):
    string = str(frase)
    contador = 0
    teste = 0
    while contador<len(string):
        if string[contador]==letra:
            if contador==num:
                return contador
        contador = contador+1
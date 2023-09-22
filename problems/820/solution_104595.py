def posLetra(frase, letra, num):
    string = str(frase)
    contador = 0
    teste = 0
    while contador<len(string):
        if contador==num:
            if string[contador]==letra:
                return contador
            
        contador = contador+1
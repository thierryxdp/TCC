def posLetra(frase, letra, num):
    string = str(frase)
    contador = 0
    teste = 0
    while contador<len(string):
        if string[contador]==letra:
            if teste==num:
                return contador
        	teste = teste+1
        contador = contador+1
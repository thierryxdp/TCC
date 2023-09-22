def posLetra(frase, letra, num):
    frase = []
    contador = 0
    while contador<len(frase):
        if frase[contador]==letra:
                return contador
        contador = contador+1
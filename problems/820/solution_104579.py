def posLetra(frase, letra, num):
    string = str(frase)
    contador = 0
    while contador<len(string):
        if string[contador]=='letra':
            return contador
        contador += 1
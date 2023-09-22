def posLetra(frase, letra, num):
    string = str(frase)
    contador = 0
    soma = 0
    while contador<len(string):
        if string[contador]==letra:
                soma = soma+1
                if soma==num:
                    return contador
        contador = contador+1
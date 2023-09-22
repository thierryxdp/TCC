def uppCons(frase):
    i=0
    vogais='AEIOUaeiou'
    while i<len(frase):
        if frase[i] != vogais:
            resultado = frase.upper
        if frase[i] == vogais:
        	resultado = frase
        i=i+1
    return resultado
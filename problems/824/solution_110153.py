def uppCons(frase):
    i=0
    vogais='AEIOUaeiou'
    while i<len(frase):
        if frase[i] != vogais[i]:
            resultado = frase[i].upper()
        if frase[i] == vogais[i]:
        	resultado = frase
        i=i+1
    return resultado
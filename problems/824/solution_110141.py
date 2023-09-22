def uppCons(frase):
    i=0
    while i+1<len(frase):
        if frase[i] != 'AEIOUaeiou':
            resultado = frase.upper
        if frase[i] == 'AEIOUaeiou':
        	resultado = frase
        i=i+1
    return resultado
def uppCons(frase):
    i=0
    resultado=0
    while i<len(frase):
        if frase[i] != 'AEIOUaeiou':
            resultado = str.upper(resultado)
        else:
            return 'a'
def uppCons(frase):
    ''' '''
    contador=0
    novafrase=' '
    while contador<len(frase):
        if frase[contador]not in 'AEIOUaeiouãõáéíóúâêîôû' and frase[contador] != frase[0]:
            novafrase= novafrase+ str.upper(frase[contador])
        if frase[contador]in 'AEIOUaeiouãõáéíóúâêîôû' and frase[contador] != frase[0]:
            novafrase= novafrase+ str.lower(frase[contador])
        if frase[contador]== frase [0]:
            novafrase=novafrase+frase[contador]
        contador=contador+1
    return novafrase
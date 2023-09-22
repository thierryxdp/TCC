def uppCons(frase):
    ''' '''
    contador=0
    novafrase=' '
    while contador<len(frase):
        if frase[contador]not in'AEIOUaeiouãõáéíóúâêîôû':
            novafrase= novafrase+ str.upper(frase[contador])
        elif frase[contador]in'AEIOUaeiouãõáéíóúâêîôû':
            novafrase= novafrase+ str.lower(frase[contador])
        contador=contador+1
    return novafrase
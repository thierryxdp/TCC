def uppCons(frase):
    cont = 0
    consoantes = ''
    while cont < len(frase):
        if frase[cont] not in 'AEIOUaeiou':
            frase[cont].upper
            frase.replace(frase[cont])
        
        if frase[cont] in 'AEIOUaeiou':
            frase[cont]
        cont = cont +1
    return frase
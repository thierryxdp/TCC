def uppCons(frase):
    cont = 0
    consoantes = ''
    while cont < len(frase):
        if frase[cont] not in 'AEIOUaeiou':
            consoantes += frase[cont].upper()
           
        if frase[cont] in 'AEIOUaeiou':
            consoantes += frase[cont]
        cont = cont +1
    return consoantes
def uppCons(frase):
    cont = 0
    consoantes = ''
    while cont < len(frase):
        if frase[cont] not in 'AEIOUaáâãeéiou':
            consoantes += frase[cont].upper()
           
        else:
            consoantes += frase[cont]
        cont = cont +1
    return consoantes
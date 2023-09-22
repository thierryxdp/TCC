def uppCons(frases):
    t=0
    consoantes=''
    while t<len(frases):
        if frase[t] not in 'AEIOUaeiouÁÉÍÓÚáéíóúãÃ:
            consoantes=consoantes + str.upper(frase[t])
            t =t+1
        elif t<len(frase):
            frase[t] in 'AEIOUaeiouÁÉÍÓÚáéíóúãÃ'
            consoantes=consoantes+frase[t]
            t=t+1
    return consoantes
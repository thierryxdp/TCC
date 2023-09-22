def conta_frases(texto):
    sinal=['.','?','!','...']
    a=0
    frases=0
    for i in range(len(sinal)):
    	a=str.count(texto,sinal[i])
        frases=frases+a
    return frases
def conta_frases(texto):
    sinal=['.','?','!']
    a=0
    frases=0
    for j in range(len(texto)-4):
        if texto[j]==texto[j+1]==texto[j+2] and texto[j]==sinal[0] and texto[j]!=len(texto):
            texto=texto[:j+1]+texto[j+3:]
        if texto[j]==len(texto):
            texto=texto
    for i in range(len(sinal)):
    	a=str.count(texto,sinal[i])
        frases=frases+a
    return frases
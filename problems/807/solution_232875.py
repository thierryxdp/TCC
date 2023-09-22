def conta_frases(frase):
    qtf=0
    for i in range(len(frase)):
        if i in ['.','!','...','?']:
            qtf+=1
            return qtf
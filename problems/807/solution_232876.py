def conta_frases(frase):
    qtf=[]
    for i in range(len(frase)):
        if i in ['.','!','...','?']:
            qtf+=i
            return len(qtf)
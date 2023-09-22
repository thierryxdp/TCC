def conta_frases(frases):
    arrayFrases = []
    ultimoFatiamento = 0
    for i in range(len(frases)-1):
        if (frases[i] == "!") or (frases[i] == "?"):
            arrayFrases.append(frases[ultimoFatiamento:i+1])
            ultimoFatiamento = i+1
        if (frases[i] == "."):
            if (i == len(frases)):
            	if (frases[i+1] == ".") and (frases[i+2] == "."):
                	arrayFrases.append(frases[ultimoFatiamento:i+3])
                	ultimoFatiamento = i+3
            	elif (frases[i+1] != ".") or (frases[i+2] != "."):
                	arrayFrases.append(frases[ultimoFatiamento:i+1])
                	ultimoFatiamento = i+1
    return len(arrayFrases)
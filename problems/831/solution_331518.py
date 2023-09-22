def lingua_p(palavra):
    palavra = str.lower(palavra)
    pf = ""
    for elemento in palavra:
        pf = pf + elemento
        if elemento in "aeiouáéíóúâêîôû":
        	pf = pf + "p" + elemento
    return pf
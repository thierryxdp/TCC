def conta_frases(frase):
    qnt_palavras = 0
    
    for digito in frase:
        if (digito == '!' or digito == '?' or digito == '.') and (frase[frase.index(digito)+1] != '.' and frase[frase.index(digito)-1] != '.'):
            qnt_palavras += 1
            	
    return qnt_palavras
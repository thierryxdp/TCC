def conta_frases(frase):
    qnt_palavras = 0
    for n in frase:
        if (n == '!' or n == '?' or n == '.') and n+1 != '.':
            
            qnt_palavras += 1
    return qnt_palavras
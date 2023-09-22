def conta_frases(frase):
    qnt_palavras = 0
    
    if frase[::-1] == '?' or frase[::-1] == '!' or frase[::-1] == '.' and frase[frase.index-1] != '.':
        qnt_palavras +=1
            
    return qnt_palavras
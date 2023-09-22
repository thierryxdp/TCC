def conta_frases(frase):
    qnt_palavras = 0
    
    if frase[::-1] == '?':
        qnt_palavras +=1
            
    return qnt_palavras
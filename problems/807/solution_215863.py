def conta_frases(frase):
    qnt_palavras = 0
    for i in frase[::-1]:
    	if i == '?' or i =='!' or i == '.' and frase[frase.index(i)-2] != '.':
        	qnt_palavras +=1
            
    return qnt_palavras
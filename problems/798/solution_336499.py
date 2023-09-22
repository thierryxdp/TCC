def freq_palavras(frases):
    ''' Entrada: Frases -> Dado do tipo string
    	
        Saída: Dicionario onde cada palavra dessa string seja uma 
        	  chave e tenha como valor o número de vezes que a 
              palavra aparece
              
        str -> dict'''
    dicionario = {}
    frases = frases.split()
    for i in range(len(frases)):
        dicionario[frases[i]] = frases.count(frases[i])
    return dicionario
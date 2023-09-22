def freq_palavras(frases):
    ''' Entrada: Frases -> Dado do tipo string
    	
        Saída: Dicionario onde cada palavra dessa string seja uma 
        	  chave e tenha como valor o número de vezes que a 
              palavra aparece
              
        str -> dict'''
    dicionario = {}
    i=0
    for palavra in frases:
        dicionario.append({palavra:i})
        n+=1
    return dicionario
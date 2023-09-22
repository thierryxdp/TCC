"""Dada uma frase a função apresenta quantas vezes as palavras aparecem"""
def freq_palavras(frases):
    palavras = frase.split()
    dict1 = {}
    counter = 0
    
    for elementos in palavras:
        dict1[palavras[counter]] = palavras.count(palavras[counter])
        counter += 1
        
	return dict1
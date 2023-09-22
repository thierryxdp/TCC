def freq_palavras(frases):
    ''' dado uma frase, retorna o número de vezes que cada palavra foi usada
    str --> dict'''
    
    freq = dict()
    palavras = str.split(frases, ' ')
    
    for palavra in palavras:
        if palavra in freq:
            freq[palavra] += 1
        else:
            freq[palavra] = 1
            
    return freq
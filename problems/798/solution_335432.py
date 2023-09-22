def freq_palavras(frases):
    '''recebe uma string com uma frase e retorna uma dicionario
    com a quantidade que cada uma das palavras aparece.
    string --> dict'''
    
    lista_frases = frases.split()
    freq = {}
    
    for palavras in lista_frases:
        if palavras in freq:
            freq = freq + 1
            
    return freq
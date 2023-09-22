def freq_palavras(frases):
    '''
    	essa função recebe uma string e retorna a frequência de vezes que cada palavra
        aparece na frase como valor do número de repetições
        str-> dicio
    '''
    x = {}
    for el in frases:
        if el in x:
            x[el] = x[el] + 1
    return x
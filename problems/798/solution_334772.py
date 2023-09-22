def freq_palavras(frase):
    '''
    	essa função recebe uma string e retorna a frequência de vezes que cada palavra
        aparece na frase como valor do número de repetições
        str-> dicio
    '''
    x = {}
    for el in frase:
        x = x + frase[el]
    return x
def freq_palavras(frases):
    '''
    	A função recebe uma string e retorna um dicionário que relaciona as palavras
        da string com o número de vezes que essa aparece na string. Considera-se que
        cada palavra esteja separada por espaços, não havendo pontuação.
        frases -> str (sem pontuação somente palavras e espaços)
        str -> dict
    '''
    frases = frases.split()
    d = {}
    for chave in frases:
        if not(chave in d):
        	d[chave] = frases.count(chave)
    return d
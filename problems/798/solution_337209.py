def freq_palavras(frases):
    '''
    	Funcao que recebe uma string e retorna um dicionario
        onde cada palavra dess string seja uma chave e tenha
        como valor o numero de vezes que a palavra aparece
        str -> dict
    '''
    dicio = {}
    x = frases.split()
    for pal in frases:
        dicio[pal] = pal.count(pal)
    return dicio
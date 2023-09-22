def freq_palavras(frases):
    ''' função que define quantas vezes uma palavra apareceu em uma determinada frase
    	str ---> dict'''
    a = {}
    frases = str.split(frases)
    for palavra in frases:
        a[palavra] = list.count(frases,palavra)
        
    return a
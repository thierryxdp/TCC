def freq_palavras(frases):
    ''' função que define quantas vezes uma palavra apareceu em uma determinada frase
    	str ---> dict'''
    a = {}
    b = {}
    frases = str.split(frases)
    for palavra in frases:
        b[palavra] = list.count(frases,palavra)
        
    return dict.items(a)
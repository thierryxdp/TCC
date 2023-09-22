def freq_palavras(frases):
    '''Recebe uma string e retorna um dicionário onde cada palavra da string é uma chave cujo valor seja o número de vezes que a palavra aparece; string->dict'''
    dicionario={}
    frases2=str.split(frases)
    for palavra in frases2:      
        dict[palavra]=dict.get(dicionario,palavra,0)+1
    return dicionario
def freq_palavras(frases):
    """ função que recebe uma string como entrada e retorna um dicionário
    	com cada palavra da string, valendo como chave e tenha um valor numérico
        de vezes que a palavra aparece. str --> dict """
    
    listaPalavra = str.split(frases, " ")
    palavraQuant = {}
    for palavra in listaPalavra:
        palavraQuant [palavra] = list.count (listaPalavra, palavra)
    return palavraQuant
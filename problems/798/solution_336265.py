def freq_palavras(frases):
    """
    	Função que retorna um dicionário com o número de 
        vezes em que cada palavra da frase dada aparece.
    	string -> dicio
    """
    dic = {}
    for palavras in frases.split():
        repeticoes = frases.count(palavras)
        dic[palavras]=repeticoes
    return dic
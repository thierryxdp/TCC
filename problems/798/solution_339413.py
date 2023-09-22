def freq_palavras(frases):
    """A função realiza a soma do numero de veses que uma palavra aparece na frase"""
    frase_fim=frases.lower()
    
    frase=frase_fim.split()
    dic = {}

    for palavra in frase:
        dic[palavra] = dic.get(palavra,0) + 1
    return dic
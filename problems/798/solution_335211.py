def freq_palavras(frases):
    """Recebe uma string e retorna um dicionário no qual cada palavra
    dessa string seja uma chave e tenha como valor o número de vezes
    que a palavra aparece;
    str -> dict"""
    palavras = frases.split()
    freq = {}
    for palavra in palavras:
        if palavra not in freq:
            freq[palavra] = 1
        else:
            freq[palavra] = freq.get(palavra) + 1
    return freq
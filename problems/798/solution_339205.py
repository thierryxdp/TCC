def freq_palavras(frases):
    dicionario = {}
    soma = 0
    for palavra in str.split(frases):
        n = list.count(palavra, frases)
        soma = soma + n
    return n
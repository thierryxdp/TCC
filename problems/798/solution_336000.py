def freq_palavras(frases):
    """retorna um dicionário com o número de vezes que cada palavra aparece"""
    dic = {}
    i = 0
    frases = str.split(frases,' ')
    while i < len(frases):
        palavra = frases[i]
        quant = list.count(frases,palavra)
        dic[palavra]=quant
        i=i+1
    return dic
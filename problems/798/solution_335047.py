def freq_palavras(frases):
    """Funcao que retorna quantas vezes cada palavra da frase aparece nessa expressao
    string --> dicionario"""
    dicionario = {}
    x = str.split(frases," ")
    for i in range(len(x)):
        y = dict.keys(dicionario)
        if x[i] in y:
            z = dicionario[x[i]] 
            dicionario[x[i]] = z + 1
        elif x[i] not in y:
            dicionario[x[i]] = 1
    return dicionario
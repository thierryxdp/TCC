def freq_palavras(frases):
    """Funcao que retorna quantas vezes cada palavra da frase aparece nessa expressao
    string --> dicionario"""
    dicionario = {}
    x = str.split(frases)
    for i in range(len(frases)):
        y = dict.keys(dicionario)
        if frases[i] in y:
            dicionario[frases[i]] = z
            dicionario[frases[i]] = z + 1
        elif frases[i] not in y:
            dicionario[frases[i]] = 1
    return dicionario
def freq_palavras(frases):
    """função qu8e recebe uma string
    e retorna um dicionário onde cada palavra da string da string
    seja uma chave e tenha como valor o número de vezes que a palavra
    aparece string -> dict"""
    dicionario = {}
    frases = frases.split()
    for i in range(len(frases)):
        dicionario[frases[i]] = frases.count(frases[i])
    return dicionario
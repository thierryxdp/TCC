def freq_palavras(frase):
    """Retorna a frequencia de cada palavra de um texto: str --> dict"""
    dici = {}
    frases = frase.split()
    for palavra in frases:
        if palavra in frases:
            soma = frases.count(palavra)
            dici[palavra] = soma
    return dici
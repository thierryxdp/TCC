def freq_palavras(frases):
    """Retorna na forma de dicionário a quantidade de vezes em que cada palavra aparece numa dada frase.
    Entrada: str
    Saída: dict
    """
    resposta = {}
    contagem = 0
    palavras = str.split(frases)
    while contador < len(palavras):
        dicionario[palavras[contagem]] = list.count(palavras, palavras[contagem])
        contagem += 1
    return resposta
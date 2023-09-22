def freq_palavras(frases):
    """Dada uma frase, a função irá retornar a quantidade
    de vezes que cada palavra se repetiu dentro da frase.
    Tipo da variável frases: string
    Tipo da saída:  """
    dicionario_frases = {}
    repeticoes = 0
    for contador in range(len(frases)):
        for contagem in range(len(frases)):
            if frases[contador] == frases[contagem]:
                repeticoes = repeticoes + 1
                dicionario_frases[frases[contador]]: repeticoes
	return dicionario_frases
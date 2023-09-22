def freq_palavras(frases):
    """Dada uma frase, a função irá avaliar a quantidade de vezes que
    cada palavra se repetiu dentro da frase e irá retornar as frases
    seguido da quantidade de repetições em formato de um dicionário.
    Tipo da variável frases: string
    Tipo da saída: dictionary"""
    divisao_palavras = frases.split()
    dicionario_frases = {}
    for contador in range(len(divisao_palavras)):
        repeticoes = 0
        if divisao_palavras[contador] not in dicionario_frases:
            for contagem in range(len(divisao_palavras)):
                if divisao_palavras[contador] == divisao_palavras[contagem]:
                    repeticoes = repeticoes + 1
			dicionario_frases[divisao_palavras[contador]] = repeticoes
	return dicionario_frases
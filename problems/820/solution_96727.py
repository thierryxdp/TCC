def encontrar(frase, letra, posicao_letra):
    posicao = str.find(frase, letra)
    posicao2 = posicao
    lugar = primeiro
    while primeiro and lugar < posicao_letra:
        posicao2 = posicao
        posicao = str.find(frase, letra, posicao + 1, len(frase) - 1)
        primeiro = 1 if not posicao == -1 else 0
        lugar += primeiro
    return posicao
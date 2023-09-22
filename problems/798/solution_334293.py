# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frases):
    d = {}
    for palavra in frases.split():
        if palavra not in d:
            d[palavra] = 1
        else:
            d[palavra] += 1
    return palavra
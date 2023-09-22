# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frases):
    dicionario = {}
    for i in frases:
        x = frases.count(i)
        dicionario[str(i)] = x
    return dicionario
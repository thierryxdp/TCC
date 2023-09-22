# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frases):
    frequencias = {}
    palavras = frases.split()
    for palavra in palavras:
        if palavra in frequencias:
            frequencias[palavra] = frequencias[palavra] + 1
        else:
            frequencias[palavra] = 0
    return frequencias
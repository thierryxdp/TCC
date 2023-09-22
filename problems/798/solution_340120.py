# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis

def freq_palavras(frases):
    x = frases.split()
    dicionario = {}
    for palavra in x:
        dicionario[palavra] = dicionario[palavra] + 1
    return dicionario
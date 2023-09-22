# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis

def freq_palavras(frases):
    x = frases.split(" ")
    lista = []
    for item in x:
        lista.append(0)
    dicionario = dict(zip(x, lista))
    for palavra in x:
        dicionario[palavra] = dicionario[palavra] + 1
    return dicionario
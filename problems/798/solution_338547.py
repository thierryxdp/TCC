# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis

def freq_palavras(frases):
    d = {}
    palavras = str.split(frases)
    for i in palavras:
        d[i] = list.count(palavras, i)
    return d
# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis

def freq_palavras(frases):
    d={}
    palavras=str.split(frases)
    for palavra in palavras:
        d[palavra]=list.count(palavras,palavra)
    return d
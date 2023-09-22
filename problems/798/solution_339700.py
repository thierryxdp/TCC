# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frases):
    F={}
    for palavras in frases:
        if palavras in F:
            F[palavras] += 1
        else:
            F[palavras] = 1
    return F
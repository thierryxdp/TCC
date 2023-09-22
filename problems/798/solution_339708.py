# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frases):
    #essa fução irá retornar um dicionário
    F={}
    #criei um segmento F para ser o dicionário
    frases=frases.split()
    #usei a função split() para listar as palavras da frase
    for palavras in frases:
        if palavras in F:
            F[palavras] += 1
        else:
            F[palavras] = 1
    return F
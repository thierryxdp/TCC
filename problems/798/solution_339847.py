# Coloque um comentário dizendo o que a função faz
def freq_palavras(frases):
    frase = frase.split(frase)
    cont = 0
    for i in range(len(frases)):
        if i > 0 and frases[i] == frases[i - 1]:
            cont += 1
            return cont
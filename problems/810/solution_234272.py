""""""
def retira_pontuacao(frase):
    pontuacao = [',', '.', ';', ':', '!', '?', '-', '...']
    for i in range(8):
        if pontuacaco[i] in frase:
            frase = frase.replace(pontuacao[i], ' ')
def inverte(frase):
    retira_pontuacao(frase)
    frase.lower()
    frase.split(frase, ' ')
    frase.join(' ', -1)
    return frase
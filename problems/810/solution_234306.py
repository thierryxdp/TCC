""""""
def retira_pontuacao(frase):
    pontuacao = [',', '.', ';', ':', '!', '?', '-', '...']
    for i in range(8):
        if pontuacao[i] in frase:
            frase = frase.replace(pontuacao[i], ' ')
    return frase
def inverte(string):
    separa = string.split()
    inverter = separa[::-1]
    junta = str.join(' ', inverter)
    return (retira_pontuacao(junta).lower()).strip()
""""""
def retira_pontuacao(frase):
    pontuacao = [',', '.', ';', ':', '!', '?', '-', '...']
    for i in range(8):
        if pontuacao[i] in frase:
            frase = frase.replace(pontuacao[i], ' ')
    return frase
def inverte(string):
    pont = (retira_pontuacao(junta).lower()).strip()
    separa = pont.split()
    inverter = separa[::-1]
    return str.join(' ', inverter)
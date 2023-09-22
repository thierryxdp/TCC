"""Recebe uma frase e retorna a mesma coma substituição da pontuação por
espaços
str->str"""

def retira_pontuacao(frase):
    pont_in_frase = ''
    pontuacao = [',', '.', ';', ':', '!', '?', '-', '...']
    for i in range (8):
        if pontuacao[i] in frase:
            frase = frase.replace(pontuacao[i], ' ')
    return frase
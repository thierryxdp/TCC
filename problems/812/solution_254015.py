"""Recebe uma string e retorna a mesma com a substituição da pontuação por
espaços
str->str"""

def retira_pontuacao(frase):
    pontuacao = [".", "...", ",", ";", ":", "!", "?", "—"]
    for i in range(8):
        if pontuacao[i] in frase:
            frase.replace(pontuacao[i], " ")
        return frase
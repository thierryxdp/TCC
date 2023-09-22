"""Recebe uma string e retorna a mesma com a substituição da pontuação por
espaços
str->str"""

def retira_pontuacao(frase):
    pontuacao = [".", "...", ",", ";", ":", "!", "?", "—"]
    frase2 = ""
    for i in range(8):
      	if pontuacao[i] in frase:
            frase2 = frase2 + frase.replace(pontuacao[i], " ")
    return frase2
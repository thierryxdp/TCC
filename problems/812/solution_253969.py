"""Recebe uma string e retorna a mesma com todas as pontuações substituídas
por espaço
str->str"""

def retira_pontuacao(frase):
    pontuacao = (".", ",", ";", ":", "!", "?", "...", "—")
    for i in range(8):
        if pontuacao[i] in frase:
        	frase2 = frase.replace(pontuacao[i], " ")
		return frase2
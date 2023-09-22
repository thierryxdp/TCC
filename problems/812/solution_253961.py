"""Recebe uma string e retorna a mesma com todas as pontuações substituídas
por espaço
str->str"""

def retira_pontuacao(frase):
    pontuacao = (".", ",", ";", ":", "!", "?", "...", "—")
	return frase.replace(pontuacao, " ")
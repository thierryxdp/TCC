"""Recebe uma string e retorna a mesma com todas as pontuações substituídas
por espaço
str->str"""

def retira_pontuacao(frase):
    pontuacao = [".", ",", ";", ":", "!", "?", "...", "—"]
	frase2 = frase.replace(pontuacao, " ")
    return frase2
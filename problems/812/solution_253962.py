"""Recebe uma string e retorna a mesma com todas as pontuações substituídas
por espaço
str->str"""

def retira_pontuacao(frase):
    pontuacao = (".", ",", ";", ":", "!", "?", "...", "—")
    for i in range(i=0, i<8, i++):
        frase.replace(pontuacao[i], " ")
	return frase
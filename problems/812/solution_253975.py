"""Recebe uma string e retorna a mesma com todas as pontuações substituídas
por espaço
str->str"""

def retira_pontuacao(frase):
    pontuacao = (".", ",", ";", ":", "!", "?", "...", "—")
    for i in range(8):
    	return frase.replace(frase, pontuacao[i], " ")
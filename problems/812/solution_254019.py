"""Recebe uma string e retorna a mesma com a substituição da pontuação por
espaços
str->str"""

def retira_pontuacao(frase):
    pontuacao = [".", "...", ",", ";", ":", "!", "?", "—"]
    for i in range(8):
    	frase2 = ""    
    	if pontuacao[i] in frase:
            frase2 = frase2 + frase.replace(pontuacao[i], " ")
    return frase2
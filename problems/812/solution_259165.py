def retira_puntuacao(frase):
    """retira todas pontuacoes de uma frase
    str->str"""
    punct = string.punctuation
for c in punct:
    frase = frase.replace(c, "")
print(frase)
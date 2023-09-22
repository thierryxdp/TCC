def retira_pontuacao(frase) 
punct = string.punctuation
for c in punct:
    s = s.replace(c, "")
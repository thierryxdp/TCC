def retira_pontuacao(frase):

s = "string. With. Punctuation?"

punct = string.punctuation
for c in punct:
    frase_nova = frase_nova.replace(c, "")
return(frase_nova)
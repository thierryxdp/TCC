def inverte(frase):
    frasepica=str.split(retira_pontuacao(frase), " ")
    frasepica=str.join(" ",frasepica[::-1])
    return str.replace(str.lstrip(frasepica.lower()),"  "," ")
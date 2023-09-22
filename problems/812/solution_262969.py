def retira_pontuacao(frase):
    frase = "-,:;."
    for i in range(0,len(frase)):
        frase = frase.replace(frase[i],"")
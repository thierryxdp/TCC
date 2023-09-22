def retira_pontuacao(frase):
    frase = "-,:;."
    for i in range(0,len(frase)):
        frase = a.replace(frase[i],"")
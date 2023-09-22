def retira_pontuacao(frase):
    x = "-,:;!?."
    y = "       "
    transtable = frase.maketrans(x,y);
    print (frase.translate(transtable))
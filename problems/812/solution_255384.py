def retira_pontuacao(frase):
    x = str("-,:;!?.")
    y = str("       ")
    transtable = frase.maketrans(x,y);
    print (frase.translate(transtable))
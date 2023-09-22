def retira_pontuacao(frase):
    x = [','':'';''!''?''.']
    y = ['']
    table = frase.maketrans(x,y);
    print (frase.translate(table))
def retira_pontuacao(frase):
    ''' funcao que retorne a frase sem caracteres de pontuacao'''
    x = "- . : ; ! ? ,"
    y = "             "
    table = frase.maketrans(x,y);
    print (frase.translate(table))
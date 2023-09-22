def retira_pontuacao (frase):
    f1 = str.replace (frase, '-', " ")
    f2 = str.replace (frase, '.', " ")
   
    return f1 + f2
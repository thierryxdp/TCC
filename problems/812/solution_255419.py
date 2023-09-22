def retira_pontuacao(frase):
    a="-,:;."
    b= "   "
    table = frase.maketrans(a,b);
    print(frase.translate(table))
def retira_pontuacao(frase):
    caracter1='!,'
    caracter2=','
    caracter=caracter1+caracter2
    return str.replace(frase,caracter1,' ')
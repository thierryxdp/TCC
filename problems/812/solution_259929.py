def retira_pontuacao(frase):
    caracter1=str('!')+str(',')
    caracter2=str(',')
    caracter3=str('.')
    return str.replace(frase,caracter1,' ')
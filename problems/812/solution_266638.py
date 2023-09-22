def retira_pontuacao(frase):
    frase = str.split(frase,'-'), str.split(frase,','), str.split(frase,':'), str.split(frase,'.'), str.split(frase,';')
    str.join(frase,' ')
    return frase
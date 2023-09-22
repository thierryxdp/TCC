def retira_pontuacao(frase):
    frase = str.split(frase,'-'),str.split(frase,':'),str.split(frase,','),tr.split(frase,'.'),tr.split(frase,';')
    return str.join(frase,' ')
def retira_pontuacao(frase):
    'dado um texto, remove todas as pontuações'
    frase=str.replace(frase,'...',' ')
    frase=str.replace(frase,'.',' ')
    frase=str.replace(frase,'-',' ')
    frase=str.replace(frase,',',' ')
    frase=str.replace(frase,'.',' ')
    frase=str.replace(frase,':',' ')
    frase=str.replace(frase,';',' ')
    frase=str.replace(frase,'?',' ')
    frase=str.replace(frase,'!',' ')
    return frase
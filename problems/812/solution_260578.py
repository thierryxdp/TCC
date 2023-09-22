def retira_pontuacao(frase):
    frase1=(((frase.replace('.',' ').replace('!',' ')).replace(',',' ')).replace('-',' ')).replace('?',' ')
    return frase1
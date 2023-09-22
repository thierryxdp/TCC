def retira_pontuacao(frase):
    nova_frase = str.replace(frase,frase[-1],' ')
    nova_frase1 = str.replace(nova_frase,'-',' ')
    nova_frase2 = str.replace(nova_frase1,',',' ')
    nova_frase3 = str.replace(nova_frase2,':',' ')
    nova_frase4 = str.replace(nova_frase3,';',' ')
    return nova_frase4
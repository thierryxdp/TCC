def retira_pontuacao(frase):
    l = frase.replace('.', '')
    l2 = l.replace(',','')
    l3 = l2.replace('-', '')
    l4 = l3.replace(':', '')
    l5 = l4.replace(';', '')
    return l5
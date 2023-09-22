def retira_pontuacao(frase):
    """Função que remove a pontuação de uma frase; str->str"""
    ponto= frase.replace('!','.')
    ponto2= ponto.replace('?','.')
    ponto3= ponto2.replace('...','.')
    ponto4= ponto3.replace('-','.')
    ponto5= ponto4.replace(':','.')
    ponto6= ponto5.replace(',','.')
    ponto7= ponto6.replace(';','.')
    frases=ponto7.replace('.',' ')
    return frases
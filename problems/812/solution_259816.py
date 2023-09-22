def retira_pontuacao(frase):
    '''retira qualquer tipo de pontuaçao da frase,str->str'''
    s_pontuacao=frase
    s_pontuacao=s_pontuacao.replace('.',' ')
    s_pontuacao=s_pontuacao.replace('...',' ')
    s_pontuacao=s_pontuacao.replace(',',' ')
    s_pontuacao=s_pontuacao.replace('!',' ')
    s_pontuacao=s_pontuacao.replace('?',' ')
    s_pontuacao=s_pontuacao.replace('-',' ')
    return s_pontuacao
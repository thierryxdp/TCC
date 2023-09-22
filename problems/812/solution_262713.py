def retira_pontuacao(frase):
    '''funcao que substitui pontuacoes por espacos.str->str'''
    return str.replace(frase,'.',' ') and str.replace(frase,',',' ') and str.replace(frase,'?',' ')
    and str.replace(frase,'!',' ')
def retira_pontuacao(frase):
    '''c'''
    resposta=''
    resposta=str.replace(frase,'.',' ')
    resposta=str.replace(frase,'!',' ')
    resposta=str.replace(frase,'?',' ')
    resposta=str.replace(resposta,',',' ')
    resposta=str.replace(resposta,'-',' ')
    resposta=str.replace(frase,':',' ')
    resposta=str.replace(frase,';',' ')
    return reposta
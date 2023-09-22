def retira_pontuacao(x):
    '''retira a pontuação presente em uma frase'''
    frase=x.replace('-','').replace(',','').replace(':','').replace(';','').replace('?','').replace('!','').replace('.',"")
    return frase
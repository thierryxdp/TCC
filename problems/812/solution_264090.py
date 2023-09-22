def retira_pontuacao(frase):
    '''c'''
    caract_pont=('.','!','?',',',':',';')
    return str.replace(frase,caract_pont,' ')
def retira_pontuacao(frases):
    '''comente'''
    string=frases
    string= str.replace('!',' ')
    string= str.replace(':',' ')
    string= str.replace('.',' ')
    return string
def retira_pontuacao(frases):
    '''comente'''
    string=frases
    string= str.replace(frases,'-',' ')
    string= str.replace(frases,',','')
    string= str.replace(frases,'!',' ')
    string= str.replace(frases,'?',' ')
    string= str.replace(frases,'.',' ')
    return string
def retira_pontuacao(txt):
    '''Dada um texto, tal funcao ira tirar todos os caracteres especiais
        str-> str'''
    x = txt.replace('-',' ')
    x = x.replace(',',' ')
    x = x.replace(':',' ')
    x = x.replace(';',' ')
    x = x.replace('.',' ')
    x = x.replace('!',' ')
    x = x.replace('?',' ')
    return x
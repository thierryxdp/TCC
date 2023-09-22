def retira_pontuacao(f):
    '''Dada uma frase, retorna a frase com pontuações substituidas por espaço.
assinatura: string --> string'''
    return str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(f,'-',' '),':',' '),'?',' '),'!',' '),',',' '),'.',' ')
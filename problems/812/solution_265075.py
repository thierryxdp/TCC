def retira_pontuacao(x):
    '''
    
    '''
    a=x.str.replace('/',' ').str.replace(',',' ').str.replace(':',' ').str.replace(';',' ').str.replace('.',' ')
    return a
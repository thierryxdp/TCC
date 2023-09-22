def retira_pontuacao(x):
    '''
    
    '''
    a=x.str.replace(x,'/',' ').str.replace(x,',',' ').str.replace(x,':',' ').
    str.replace(x,';',' ').str.replace(x,'.',' ')
    return a
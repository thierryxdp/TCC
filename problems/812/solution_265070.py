def retira_pontuacao(x):
    '''
    
    '''
    a=str.replace(x,'/',' ')+str.replace(x,',',' ')+str.replace(x,':',' ')+str.replace(x,';',' ')+str.replace(x,'.',' ')
    return a
def retira_pontuacao(x):
    '''
    
    '''
    x=str.replace((x,'/','')(x,',','')(x,':','')(x,';','')(x,'.',''))
    return x
def retira_pontuacao(x):
    '''
    
    '''
    x = str.split(x, ",",":",";",".","!","?","-")
    x = str.join(" ", x)
    return x
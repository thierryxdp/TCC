def retira_pontuacao(x):
    '''
'''
    x = x.replace("."," ").replace(","," ").replace("?"," ").replace(":"," ").replace(";"," ").replace("!"," ").replace("-"," ").replace("..."," ")
    
    return x
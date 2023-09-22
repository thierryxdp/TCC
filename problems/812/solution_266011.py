def retira_pontuação(x):
    '''
'''
    x = x.replace("."," ").replace(","," ").replace("?"," ").replace(":"," ").replace(";"," ").replace("!"," ").replace("-"," ").replace("..."," ")
    
    return x
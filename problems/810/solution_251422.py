def retira(x):
    '''
'''
    x = x.replace("."," ").replace(","," ").replace("?"," ").replace(":"," ").replace(";"," ").replace("!"," ").replace("-"," ").replace("..."," ")
    
    return x


def inverta(x):
    ''
    x = retira(x.lower())
    
    a = list(x.split())
    
    a.reverse()
    return " ".join(a)
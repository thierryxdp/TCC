def conta_frases(x):
    
    
    return str.count(x,'.') + str.count(x,str.replace(x,'...','.')) + str.count(x,'!') + str.count(x,'?')
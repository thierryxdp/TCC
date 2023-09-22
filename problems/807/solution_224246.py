def conta_frases(string):

    s= string
    s=str.replace(s, '!', '.')
    s=str.replace(s, '?', '.')
    s=str. replace(s,'...', '.')
    
    

    x= str.count(s, '.')
   
    return x
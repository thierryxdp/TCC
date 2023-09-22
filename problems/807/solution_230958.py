def conta_frases(text):
    
    a= text.split('.')
    b= text.split('!')
    c= text.split('?')
    d= text.count('...')
    
    return (len(a)- 2*(d)) + len(b) + len(c) - 3
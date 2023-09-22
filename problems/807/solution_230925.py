def conta_frases(text):
    
    a= text.split('.')
    b= text.split('!')
    c= text.split('?')
    d= text.split('...')
    
    return len(a)
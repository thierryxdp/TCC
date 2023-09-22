def conta_frases(text):
    
    a= text.split('.')
    b= text.split('!')
    c= text.split('?')
    d= text.count('...')
    
    return (len(a)- 2*(len(d)) + len(b) + len(c) - 3
    print(return)
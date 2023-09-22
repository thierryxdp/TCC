def conta_frases(x):
    '''função que calcula e retorna o numero de frases em um texto dado'''
    '''str-> int'''
    "." != "..."
    a=str.count(x,"...")
    b=str.count(x,".")
    c=str.count(x,"!")
    d=str.count(x,"?")
    
    if"..."in x:
        return (a+c+d+b)-3*a
    return a+b+c+d
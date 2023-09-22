def conta_frases(frase):
    '''função que conta o número de frase que têm em um
    texto, segundo as pontuações ali presentes
    string -> string'''
    a = str.count(frase,'.')
    b = str.count(frase,'!')
    c = str.count(frase,'?')
    
   
    return a+b+c
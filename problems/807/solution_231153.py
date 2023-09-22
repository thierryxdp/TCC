def conta_frases(frase):
    '''função que conta o número de frases que têm em um texto, segundo as pontuações ali presentes
    string -> inteiro'''
    a = str.count(frase,'.') 
    b = str.count(frase,'...')
    c = str.count(frase,'!')
    d = c-(3*b)
    e = str.count(frase,'?')
    
   
    return a+b+d+e
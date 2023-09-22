def quant_frase(texto):
      '''função que conta o número de frases que têm em um texto, segundo as pontuações ali presentes
    string -> string'''
    a = str.count(texto,'.'):
    b = str.count(texto,'...')
    c = str.count(texto,'!')
    d = c-(3*b)
    e = str.count(texto,'?')
    
   
    return a+b+d+e
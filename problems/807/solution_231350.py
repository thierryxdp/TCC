def quant_frase(texto):
      '''função que conta o número de frases que têm em um texto, segundo as pontuações ali presentes
    string -> string'''
a = texto.count("."):
    b = texto.count("...")
    c = texto.count("!")
    d = c-(3*b)
    e = texto.count("?")
    
   
    return a+b+d+e
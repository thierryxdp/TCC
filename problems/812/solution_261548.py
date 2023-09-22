#Exercício_04: 
''' Essa função substitui a pontuação de uma frase por " " (espaços). '''
''' str ---> str. '''

def punctuation_elimination(string_text):
    
    a = str.replace(string_text, ",", " ")
    
    b = str.replace(a, ".", " ")
    
    c = str.replace(b, "?", " ")
    
    d = str.replace(c, "!", " ")
    
    e = str.replace(d, "-", " ")
    
    f = str.replace(e, ":", " ")
    
    g = str.replace(f, ";", " ")
    
    return g
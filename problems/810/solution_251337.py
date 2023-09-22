def inverte(texto):
    '''funcao recebe a frase e retorna 
    ela invertida sem pontuação nenhuma
    str-> str'''
    
    if ":" in texto:
        texto= texto.replace(":", " ")
    if ";" in texto:
        texto= texto.replace(";", " ")
    if "?" in texto:
        texto= texto.replace("?", " ")
    if "!" in texto: 
        texto= texto.replace("!", " ")
    if "-" in texto:
        texto= texto.replace("-", " ")
    if "." in texto:
        texto= texto.replace(".", " ")
    if "," in texto:
        texto= texto.replace(",", " ")
        
       
        
    divi= texto.split(" ") 
    total= len(divi)+1
    x= divi[-1:-(total):-1]
    juntar= str.join(' ',x)
    
    return str.lower(juntar)
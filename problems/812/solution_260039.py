def retira_pontuacao(frase):
    """A entrada será uma frase que tenha caracteres de pontuação
    e o retorno será trocar todos esses caracteres presentes no parâmetro, por espaço"""
    
    #str -> srt 
    
  
    if "-" in frase:
        frase = frase.replace ("-", " ") 
        
    elif "," in frase:
        frase = frase.replace (","," ")
        
    elif ":" in frase:
        frase = frase.replace (":", " ") 
    
    elif ";" in frase:
        frase = frase.replace (";", " ")
        
    elif "." in frase:
        frase = frase.replace (".", " ")
    
    if "!" in frase:
        frase = frase.replace ("!", " ")
    
    if "?" in frase:
        frase = frase.replace ("?", " ")
        
        return frase
def retira_pontuacao(frase):
    """A entrada será uma frase que tenha caracteres de pontuação
    e o retorno será trocar todos esses caracteres presentes no parâmetro, por espaço"""
    
    #str -> srt 
    
  
        frase = frase.replace ("-", " ")
        
        frase = frase.replace (","," ")
        
        frase = frase.replace (":", " ") 
    
        frase = frase.replace (";", " ")
        
        frase = frase.replace (".", " ")
        
        frase = frase.replace ("!", " ")
        
        frase = frase.replace ("?", " ")
        
        frase = frase.replace ("...", " ")
        
        return frase
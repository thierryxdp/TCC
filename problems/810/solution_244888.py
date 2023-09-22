def inverte (frase): 
    '''dada uma frase retorna outra frase com as palavras na ordem inversa, sem letras maiusculas e pontuacao''' '''str -> str''' 
    '''str -> str'''
    def retira_pontuacao (frase):     
        '''substitui todos os caracteres de pontuacao por espaço'''     
        '''str -> str'''            
        frase = frase.replace ("."," ")     
        frase = frase.replace (","," ")     
        frase = frase.replace ("?"," ")     
        frase = frase.replace ("!"," ")     
        frase = frase.replace ("-"," ")     
        frase = frase.replace (":"," ")     
        frase = frase.replace (";"," ")     
        return frase
    
    texto=retira_pontuacao(frase)
    str.lower(texto)
    texto = str.split(texto)
   
    
    
    
    return texto
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
    
    f_sem_pontos=retira_pontuacao(frase)
    texto = (str.split(f_sem_pontos))
    
    
    
    
    
    return texto
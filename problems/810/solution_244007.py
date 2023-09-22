def inverte (frase):
    """dada uma frase retorne uma outra frase que contenha as mesmas palavras da frase de entrada na ordem inversa, sem letras maiúsculas, e sem a pontuação. 
    
    entrada->str
    retorna->str"""
    
    frase2=str.replace (frase,'.',' ')
    frase2=str.replace (frase2,',', ' ')
    frase2=str.replace (frase2,':', ' ')
    frase2=str.replace (frase2,';',' ')
    frase2=str.replace (frase2,'?',' ')
    frase2=str.replace (frase2,'!',' ')
    frase2=str.replace (frase2,'-',' ')
    frase2= str.lower (frase2)
    frase2=str.split (frase2)
    frase2=list.reverse (frase2)
    
    return frase2
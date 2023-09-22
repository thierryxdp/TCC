def inverte(frase):
    """Retorna uma outra frase que contenha a mesmas palvras da frase de entrada na ordem inversa, sem letras maiúsculas e pontuação.
    string --> string """
	
    frase1 = str.replace(frase, '.', ' ')
    
    frase2 = str.replace(frase1, '!', ' ')
    
    frase3 = str.replace(frase2, '?', ' ')
    
    frase4 = str.replace(frase3, '...', ' ')
    
    frase5 = str.replace(frase4, '-', ' ')
    
    frase6 =  str.replace(frase5, ',', ' ')
    
    frase7 = str.replace(frase6, ':', ' ')
    
    frase8 = str.lower(str.replace(frase7, ';', ' '))
    
    frase_separada = str.split(frase8)
    
    frase_inversa = frase_separada[-1:]
    
    frase_junta = str.join(' ',frase_inversa)
    
    return frase_junta
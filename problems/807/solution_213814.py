def conta_frases(texto):
    """ 
    função que tem como entrada um texto e retorna o número de frases contidas nele
    
    string -> int 
    
    """
    texto =  str.replace(texto,'?','.')
    texto = str.replace(texto,'!','.')
    texto = str.replace(texto,'...','.')
    
    return len(str.split(texto,'.')) -1
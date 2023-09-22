def uppCons(frase):
    """A função retorna todas as consoantes de uma frase
    	em maiusula.
        str-->str"""
    consoantes =('bdfghjklmnpqrstvwxyz')
    
    if consoantes in frase:
        str.upper(consoantes)
        frase1=str.join('',consoantes)
    return frase1
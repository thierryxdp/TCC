def conta_frase(frase):
    """Retorna o numero de frases dado: um texto, sendo que 
    cada frase termina em um ponto final, ponto de exclamacao,
    de interrogacao ou 3 pontos"""
     
    frase1=str.count(frase,'...')
    frase2=str.replace(frase,'...','.')
    frase1=str.count(frase2,'?')+str.count(frase2,'!')+str.count(frase2,'.')
    
    return frase1
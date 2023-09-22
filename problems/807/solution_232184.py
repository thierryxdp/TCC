def conta_frases(S):
    """Funçao na qual conta o numero de ocorrencia de pontuaçao para entregar o numero de frases,
    str-->int
    """ 
  
    
    p=str.count(S, '.')
    e=str.count(S, '!')
    i=str.count(S, '?')
    r=str.count(S, '...')
    
    c=i-(r*3)
    
    f=p+e+c+r
    
    return f
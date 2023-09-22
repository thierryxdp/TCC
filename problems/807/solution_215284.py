def conta_frases(texto):
    """Função que retorna a quantidade de frases presentes no texto dado"""
    a = str.replace(texto,'?','#')
    b = str.replace(a,'!','#')
    c = str.replace(b,'...','#')
    d = str.replace(c,'.','#')
    e = str.count(d,'#')
    f = str.split(d,'#',(e-1))
    
    return len(f)
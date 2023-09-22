def conta_frases(texto):
    """Função que retorna a quantidade de frases presentes no texto dado"""
    if ('!' and '?' and '...' and '.') not in texto[0:len(texto)-1]:
        return 1
    else:
        x = 3 * '.'
        a = str.replace(texto,'?','#')
        b = str.replace(a,'!','#')
        c = str.replace(b,x,'#')
        d = str.replace(c,'.','#')
        e = str.count(d,'#')
        f = str.split(d,'#',(e-1))
        return len(f)
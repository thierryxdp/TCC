def uppCons(frase):
    """retorna a frase com todas as conssoantes em maiúsculo,
    e os demais carcteres como foram dados;
    strin, -> string"""
    
    s = ''
    for consoantes in frase:
        if consoantes in 'bcdfghjklmnpqrstvxwyz':
            s += consoantes.upper()
        else:
            s += consoantes
    return s
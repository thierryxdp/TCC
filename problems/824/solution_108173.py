def uppCons(frase):
    """Função que retorna a frase de entrada com todos as suas
    consoantes em maiúsculas. str -> str"""
    
    i = 0
    s = ''
    
    while i < len(frase):
        if frase[i] in ' aeiouAEIOU!?,.;ÁÉÍÓÚÀÈÌÒÙáéíóúàèìòù-ãõ':
            s = s + frase[i]
        elif frase[i] in 'bcdfghjklmnpqrstvwxyzçBCDFGHJKLMNPQRSTVWXYZÇ':
            a = str.upper(frase[i])
            s = s + a
        i+= 1
    return s
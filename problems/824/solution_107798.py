def uppCons(frase):
    """funcao que dada uma frase como entrada, retorne a frase com todas as suas consoantes em maiuscula e demais caracteres exatamente como estavam na original
    str -> str"""
    frase1 = ''
    tamanho = 0
    consoante = 'cdfghjklmnpqrstvwxyzç'
    while tamanho < len(frase):
        if frase [tamanho] in consoante:
            frase1 = frase1 +(str.upper(frase[tamanho]))
            else:
            frase1  = frase1+ frase[tamanho]
            tamanho = tamanho+1
    return frase1
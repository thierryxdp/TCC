def uppCons(frase):
    """dada uma string frase de entrada, retorna a mesma string no entanto com
    os caracteres consoantes em maiusculo
    str --> str"""
    contador=0
    while contador < len(frase):
        if frase[contador] in 'bcdfghjklmnpqrstvxywzç':
            str.replace(frase,frase[contador],str.upper(frase[contador]))
        contador=contador+1
    return frase
def conta_frases(texto):
    '''conta o número de frases que aparecem no texto
    string -> int'''
    texto1 = str.replace(texto, "...", "#")
    texto2 = str.replace(texto1, ".", "#")
    texto3 = str.replace(texto2, "!", "#")
    texto4 = str.replace(texto3, "?", "#")
    texto5 = str.replace(texto4, " ", "")
    texto6 = str.split(texto5, "#")
    num_frases = len(texto6)
    return num_frases
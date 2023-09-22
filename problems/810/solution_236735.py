def inverte(txt):
    '''Função que recebe uma string e retorna ela invertida sem letras maiúsculas
    e sem pontuação; str -> str'''
    
    txt = str.replace(txt, ".", " ")
    txt = str.replace(txt, ",", " ")
    txt = str.replace(txt, "/", " ")
    txt = str.replace(txt, ":", " ")
    txt = str.replace(txt, "-", " ")
    txt = str.replace(txt, "_", " ")
    txt = str.replace(txt, ";", " ")
    txt = str.replace(txt, "!", " ")
    txt = str.replace(txt, "?", " ")
    txt = txt.casefold()
    txt = txt.split()
    txt = txt[-1::-1]
    txt = " ".join(txt)
    
    return txt
def inverte(frase):
    """Função que ao receber uma frase, retorna uma outra frase que contém as mesmas
    palavras, mas de ordem inversas e sem pontuação;
    str -> str"""
    frasef = str.replace(str.replace(str.replace(str.replace(str.replace(frase, ',', ''), '!',''),'.',''), '?', ''),'-', ' ')
    frasef1 = str.split(frasef, ' ')
    frasef2 = str.join(' ', frasef1[::-1])
    return str.lower(frasef2)
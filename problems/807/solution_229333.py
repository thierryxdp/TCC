def conta_frases(texto):
    '''função que dado um texto, retorna a quantidade de frases contida nele;
    str -> int'''
    texto1 = texto.replace('...','#')
    texto2 = texto1.replace('!','#')
    texto3 = texto2.replace('?','#')
    texto4 = texto3.replace('.','#')
    frases = len(texto4.split('#')
    return frases
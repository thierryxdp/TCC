def conta_frases(texto):
    texto1 = texto.replace('.','/')
    texto2 = texto1.replace('!','/')
    texto3 = texto2.replace('?','/')
    texto4 = texto3.replace('...','/')
    quantidade = texto4.count('/')
    return quantidade
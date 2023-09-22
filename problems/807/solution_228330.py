def conta_frases(texto):
    texto1 = str.replace(texto,'.','/')
    texto2 = str.replace(texto1,'!','/')
    texto3 = str.replace(texto2,'?','/')
    texto4 = str.replace(texto3,'...','/')
    quantidade = texto4.count('/')
    return quantidade
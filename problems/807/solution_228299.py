def conta_frases(texto):
    if '.' in texto:
        texto1 = str.replace(texto,'.','#')
    if '!' in texto:
        texto2 = str.replace(texto1,'!','#')
    if '?' in texto:
        texto3 = str.replace(texto2,'?','#')
    if '...' in texto:
        texto4 = str.replace(texto4,'...','#')
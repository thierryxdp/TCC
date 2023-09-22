def conta_frases(texto):
    if '?' in texto:
        print (len(texto.split('?')))
    elif '.' in texto:
        print (len(texto.split('.')))
    elif '...' in texto:
        print (len(texto.split('...')))
    elif '!' in texto:
        print (len(texto.split('!')))
    else :
        print ('')
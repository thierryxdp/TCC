def conta_frases(texto):
    '''retorna o numero de frases em um texto; str -> int'''
    
    texto1 = str.count(texto,". ")
    texto2 = str.count(texto,"?")
    texto3 = str.count(texto,"...")
    texto4 = str.count(texto,"!")
    return texto1+texto2+texto3+texto4
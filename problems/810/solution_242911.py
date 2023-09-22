def inverte(frase):
    """retorna uma frase na ordem inversa"""
    frasesempt = str.strip(frase,'.')
    frasesemvirg = str.strip(str.strip(frase,'.'),',')
    frasesemexclama = str.strip(frasesemvirg,'!')
    fraseseminterroga = str.strip(frasesemexclama,'?')
    fraselower = fraseseminterroga.lower
    return fraselower
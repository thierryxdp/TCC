def inverte(frase):
    """retorna uma frase na ordem inversa"""
    frasesempt = str.strip(frase,'.')
    frasesemvirg = str.strip(str.strip(frase,'.'),',')
    frasesemexclama = str.strip(str.strip(str.strip(frase,'.'),',')'!')
    fraseseminterroga = str.stripstr.strip(str.strip(str.strip(frase,'.'),',')'!')'?')
    fraselower = fraseseminterroga.lower
    return fraselower
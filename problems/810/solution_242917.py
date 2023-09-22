def inverte(frase):
    """retorna uma frase na ordem inversa"""
    frasesempt = str.strip(frase,'.')
    frasesemvirg = str.strip(frasesempt,',')
    frasesemexclama = str.strip(frasesemvirg,'!')
    fraseseminterroga = str.strip(frasesemexclama,'?')
    return str.lower(fraseseminterroga)
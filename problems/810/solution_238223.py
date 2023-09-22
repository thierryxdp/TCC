import string
def inverte(s):
    '''dada frase, a retorna com as palavras na ordem inversa,
    sem pontuação e sem letras maiúsculas;
    string --> string'''
    for c in string.punctuation:
        s = s.replace(c,' ')
    s2 = str.split(s)
    s3 = s2[::-1]
    s4 = str.join(' ',s3)
    return str.lower(s4)
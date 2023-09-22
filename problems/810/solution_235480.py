def inverte(frase):
    minuscula= str.lower(frase)
    pontuacao= str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(minuscula,'-',' '),',',' '),':',' '),';',' '),'.',' '),'?',' '),'!',' ')
    s= str.split(pontuacao,' ')[::-1]
    """dada"""
    return str.strip(str.join(' ', s))
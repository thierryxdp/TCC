def inverte(frase):
    pontuacao= str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase,'-',' '),',',' '),':',' '),';',' '),'.',' '),'?',' '),'!',' ')
    s= str.split(frase,' ')[::-1]
    """dada"""
    return str.join(' ', s)
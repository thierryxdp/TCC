def inverte(frase):
    """essa função recebe uma frase como entrada e retorna a mesma frase, porém na ordem inversa;
    string->string"""
    frase = frase.replace(',',' ')
    frase = frase.replace('!',' ')
    frase = frase.replace('.',' ')
    frase = frase.replace('?',' ')
    frase = frase.replace('-',' ')
    frase = str.split(frase)
    frase = frase[::-1]
    frase = str.join(' ',(frase))
    frase = str.lower(frase)
    return frase
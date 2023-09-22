def inverte(frase):
        '''Retorna a frase invertida
        string -> string'''
        frase = frase.replace('-',' ')
        frase = frase.replace(':',' ')
        frase = frase.replace(';',' ')
        frase = frase.replace(';',' ')
        frase = frase.replace('.',' ')
        frase = frase.replace('!',' ')
        frase = frase.replace('?',' ')
        frase = frase.replace(',',' ')
        frase = frase.lower()
        frase = frase.split(' ')
        frase = frase[::-1]
        str.join('',frase)
        return frase
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
        frase = frase.split(' ')
        frase[::-1]
        str.join(' ',[::-1]) = frase
        return frase
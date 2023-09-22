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
        frase = str.lower(frase)
        frase 
        return frase
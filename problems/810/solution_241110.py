def inverte(frase):
        '''Retorna a frase invertida
        string -> string'''
        frase = frase.replace('-',' ')
        frase = frase.replace(':','')
        frase = frase.replace(';','')
        frase = frase.replace(';','')
        frase = frase.replace('.','')
        frase = frase.replace('!','')
        frase = frase.replace('?','')
        frase = frase.replace(',','')
        frase = frase.lower()
        frase = frase.split(' ')
        frase.join(' ')
        frase = frase[::-1]
        return frase
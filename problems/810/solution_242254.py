def inverte(frase):
    '''
       Função que recebe um frase e a retorna na ordem inversa
       sem letras maiúsculas e sem a pontuação
       str -> str
    '''
    frase= frase.replace(',',' ')
    frase= frase.replace('-',' ')
    frase= frase.replace('.',' ')
    frase= frase.replace(':',' ')
    frase= frase.replace(';',' ')
    frase= frase.replace('?',' ')
    frase= frase.replace('!',' ')
    frase=frase.lower()
    frase=frase.split()
    frase=list(frase)
    frase.reverse()
    return ' '.join(frase)
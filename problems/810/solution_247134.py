def inverte(frase):
    '''Função que retorna uma frase espaçando todos os caracteres'''
    'str -> str'
    frase==str
    #-->('!',',','.',';','?','!','-')

    if  '!' or ',' or '.' or ';' or '?' or '!' or '-' in frase:
        
        C=frase.replace('!',' ').replace(',',' ').replace('.',' ').replace(';',' ').replace('?',' ').replace('!',' ').replace('-',' ')
        reverse(C)
        return C
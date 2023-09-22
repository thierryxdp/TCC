def inverte(frase):
    '''Função que retorna uma frase espaçando todos os caracteres'''
    'str -> str'
    frase==str
    #-->('!',',','.',';','?','!','-')

    if  '!' or ',' or '.' or ';' or '?' or '!' or '-' in frase:
        frase==frase.replace('!',' ').replace(',',' ').replace('.',' ').replace(';',' ').replace('?',' ').replace('!',' ').replace('-',' ')
        return list.reverse(frase)
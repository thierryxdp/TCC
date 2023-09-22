def retira_pontuacao(frase):
    '''Função que retorna uma frase espaçando todos os caracteres'''
    'str -> str'
    frase==str
    
    if '!'  in frase:
        return  frase.replace('!', ' ')
    elif '!' and '-' in frase:
        return frase.replace('!',' ').replace('-',' ')
    
    elif ',' and '.':
        return frase.split(',','.').replace('.',' ')
    elif '?' in frase:
        return  frase.replace('?', ' ')
    elif ':' in frase:
        return  frase.replace(':', ' ')
    elif ';' in frase:
        return  frase.replace(';', ' ')
    elif '-' and '.' in frase:
        return frase.split('-','.').replace('.',' ')
    elif ',' in frase:
        return  frase.replace(',', ' ')
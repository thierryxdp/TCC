def retira_pontuacao(frase):
    '''Função que retorna uma frase espaçando todos os caracteres'''
    'str -> str'
    frase==str
    
    if '!' in frase:
        return  frase.replace('!', ' ')
    elif '.' in frase:
        return  frase.replace('.', ' ')
    
    elif '?' in frase:
        return  frase.replace('?', ' ')
    elif ':' in frase:
        return  frase.replace(':', ' ')
    elif ';' in frase:
        return  frase.replace(';', ' ')
    elif ',' in frase:
        return  frase.replace(',', ' ')
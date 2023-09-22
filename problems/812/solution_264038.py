def retira_pontuacao (frase):
    '''retorna a frase sem os caracteres de pontuação
    (travessão, vírgula, dois pontos, ponto, interrogação, exclamação, reticências),
    e substitui por um espaço
    str->str'''
    
    if '-' in frase:
        return str.replace (frase,'-',' ')
    elif ',' in frase:
        return str.replace (frase,',',' ')
    elif ':'in frase:
        return str.replace (frase,':',' ')
    elif '?' in frase:
        return str.replace (frase,'?',' ')
    elif '!' in frase:
        return str.replace (frase,'!',' ')
    elif '...' in frase:
        return str.replace (frase,'...',' ')
    elif '.' in frase:
        return str.replace (frase,'.',' ')
    else:
        return frase
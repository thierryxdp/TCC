def retira_pontuacao(frase):
    """Recebe uma frase e retorna a mesma frase só que sem os caracteres de pontuação; str->str"""
    n = '!' and '.' and '?' and ';' and ':' and '-' and ',' 
    if '!' in frase:
        return str.replace(frase, '!', ' ')
    elif '.' in frase:
        return str.replace(frase, '.', ' ')
    elif '?' in frase:
        return str.replace(frase, '?', ' ')
    elif ';' in frase:
        return str.replace(frase, ';', ' ')
    elif ':' in frase:
        return str.replace(frase, ':', ' ')
    elif '-' in frase:
        return str.replace(frase, '-', ' ')
    elif ',' in frase:
        return str.replace(frase, ',', ' ')
def retira_pontuacao(frase):
    """Funcao que substitui a pontuacao da frase
    por espaços vazios.
    str -> str"""
    
    if '?' in frase:
        lista = frase.split('?')
        return " ".join(lista)
    
    elif '.' in frase:
        lista = frase.split('.')
        return " ".join(lista)
    
    elif '!' in frase:
        lista = frase.split('!')
        return " ".join(lista)
    
    elif ',' in frase:
        lista = frase.split(',')
        return " ".join(lista)
    
    elif ':' in frase:
        lista = frase.split(':')    
        return " ".join(lista)
    
    elif ';' in frase:
        lista = frase.split(';')
        return " ".join(lista)
    
    elif '-' in frase:
        lista = frase.split('-')
        return " ".join(lista)
    
    elif '...' in frase:
        lista = frase.split('...')
        return " ".join(lista)
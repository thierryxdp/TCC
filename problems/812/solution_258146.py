def retira_pontuacao(frase):
    """retorna frase onde os caracteres de pontuação são substituidos por espaços.
    str->str"""
    if '.' in (frase):
        return str.replace((frase),'.',' ')
    
    if '!' in (frase):
        return str.replace((frase),'!',' ')
    
    if '?' in (frase):
        return str.replace((frase),'?',' ')
    
    if '...' in (frase):
        return str.replace((frase),'...',' ')
    
    if '-' in (frase):
        return str.replace((frase),'-',' ')
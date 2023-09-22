def retira_pontuacao(frase):
    """essa funçao recebe uma frase e a retorna com sinais de pontuaçao substituidos por espaço"""
    """entrada: str"""
    """saida: str"""
    if ',' in frase:
        frase = str.replace(frase,',',' ') and str.replace(frase,'.',' ')
        return frase
    elif '.' in frase:
        frase = str.replace(frase,'.',' ')
        return frase
    elif '?' in frase:
        frase = str.replace(frase,'?',' ')
        return frase
    elif '!' in frase:
        frase = str.replace(frase,'!',' ')
        return frase
    elif '-' in frase:
        frase = str.replace(frase,'-',' ')
        return frase
    elif '...' in frase:
        frase = str.replace(frase,'...',' ')
        return frase
    elif ':' in frase:
        frase = str.replace(frase,':',' ')
        return frase
    elif ';' in frase:
        frase = str.replace(frase,';',' ')
        return frase
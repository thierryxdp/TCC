def retira_pontuacao(frase):
    """essa funçao recebe uma frase e a retorna com sinais de pontuaçao substituidos por espaço"""
    """entrada: str"""
    """saida: str"""
    if '.' or ',' in frase:
        return str.replace(frase,'.' and ',',' ')
    elif '?' in frase:
        return str.replace(frase,'?',' ')
    elif '!' in frase:
        return str.replace(frase,'!',' ')
    elif '-' in frase:
        return str.replace(frase,'-',' ')
    elif '...' in frase:
        return str.replace(frase,'...',' ')
    elif ':' in frase:
        return str.replace(frase,':',' ')
    elif ';' in frase:
        return str.replace(frase,';',' ')
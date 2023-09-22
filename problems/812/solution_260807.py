def retira_pontuacao(frase):
    """essa funçao recebe uma frase e a retorna com sinais de pontuaçao substituidos por espaço"""
    """entrada: str"""
    """saida: str"""
    if '.' in frase:
        return str.replace(frase,'.',' ')
    elif '?' in frase:
        return str.replace(frase,'?',' ')
    elif '!' in frase:
        return str.replace(frase,'!',' ')
    elif ',' in frase:
        return str.split(frase, ',')
    elif '-' in frase:
        return str.split(frase,'-')
    elif '...' in frase:
        return str.replace(frase,'...',' ')
    elif ':' in frase:
        return str.replace(frase,':',' ')
    elif ';' in frase:
        return str.replace(frase,';',' ')
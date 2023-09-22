def retira_pontuacao(frase):
    """essa funçao recebe uma frase e a retorna com sinais de pontuaçao substituidos por espaço"""
    """entrada: str"""
    """saida: str"""
    if '.' in frase:
        str.strip(frase,'.')
    elif '?' in frase:
        str.strip(frase,'?')
    elif '!' in frase:
        str.strip(frase,'!')
    elif ',' in frase:
        str.strip(frase,',')
    elif '-' in frase:
        str.strip(frase,'-')
    elif '...' in frase:
        str.strip(frase,'...')
    elif ':' in frase:
        str.strip(frase,':')
    elif ';' in frase:
        str.strip(frase,';')
def retira_pontuacao(frase):
    """essa funçao recebe uma frase e a retorna com sinais de pontuaçao substituidos por espaço"""
    """entrada: str"""
    """saida: str"""
    str.replace(frase,'.',' ')
    if '?' in frase:
        return str.replace(frase,'?',' ')
    if '!' in frase:
        return str.replace(frase,'!',' ')
    if ',' in frase:
        return str.replace(frase, ',' , ' ')
    if '-' in frase:
        return str.replace(frase,'-',' ')
    if '...' in frase:
        return str.replace(frase,'...',' ')
    if ':' in frase:
        return str.replace(frase,':',' ')
    if ';' in frase:
        return str.replace(frase,';',' ')
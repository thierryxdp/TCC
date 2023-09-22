def retira_pontuacao(frase):
    """essa funçao recebe uma frase e a retorna com sinais de pontuaçao substituidos por espaço"""
    """entrada: str"""
    """saida: str"""
    str.replace(frase,'.',' ')
    str.replace(frase,'?',' ')
    str.replace(frase,'!',' ')
    str.strip(frase, ',')
    str.strip(frase,'-')
    str.replace(frase,'...',' ')
    str.replace(frase,':',' ')
    str.replace(frase,';',' ')
    return frase
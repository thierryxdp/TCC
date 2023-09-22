def retira_pontuacao(frase):
    """recebe uma frase e retorna a mesma, porém com todos seus sinais de pontação substituídos por espaço"""
    """str -> str"""
    frase=str.replace(frase,'.',' ')
    frase=str.replace(frase,'!',' ')
    frase=str.replace(frase,'?',' ')
    frase=str.replace(frase,'...',' ')
    frase=str.replace(frase,';',' ')
    frase=str.replace(frase,':',' ')
    frase=str.replace(frase,',',' ')
    frase=str.replace(frase,'-',' ')
    return frase
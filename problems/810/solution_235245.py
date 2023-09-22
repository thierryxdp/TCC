def retira_pontuacao(frase):
    """Função que retorna a frase de entrada com todos os caracteres de pontuação 
    substituidos por espaços. str->str"""
    frase1 = str.replace(frase,'-',' ')
    frase2 = str.replace(frase1,',',' ')
    frase3 = str.replace(frase2,':',' ')
    frase4 = str.replace(frase3,';',' ')
    frase5 = str.replace(frase4,'.',' ')
    frase6 = str.replace(frase5,'!',' ')
    frase7 = str.replace(frase6,'?',' ')
    return frase7
def inverte(s):
    """."""
    s1 = str.lower(retira_pontuacao(s))
    s2 = str.strip(s1,' ')
    s3 = " ".join(s2.split())
    s4 = str.split(s3,' ')
    s5 = s4[::-1]
    s6 = str.join(' ',s5)
    return s6
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
    """Função que retorna outra frase que contêm as mesmas palavras da frase de entrada
    na ordem inversa, sem pontuação e sem letras maiúsculas. str->str"""
    s1 = str.lower(retira_pontuacao(s))
    s2 = str.split(s1,' ')
    s3 = s2[::-1]
    s4 = str.join(' ',s3)
    return s4
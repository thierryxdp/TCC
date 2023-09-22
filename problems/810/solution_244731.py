def retira_pontuacao(frase):
    """função que retira todas as pontuações da frase
    str -> str"""
    frase1 = str.replace(frase,',',' ')
    frase2 = str.replace(frase1,'-',' ')
    frase3 = str.replace(frase2,':',' ')
    frase4 = str.replace(frase3,';',' ')
    frase5 = str.replace(frase4,'.',' ')
    frase6 = str.replace(frase5,'!',' ') 
    frase7 = str.replace(frase6,'...',' ')
    frase8 = str.replace(frase7,'?',' ')
    return frase8

def inverte(texto):
    """função que inverte as palavras de um texto alem de tirar as pontuações
    str -> str"""
    texto = texto[0:-1]
    texto = retira_pontuacao(str.lower(texto))
    texto = str.split(texto,)
    list = texto
    list.reverse()
    return str.join(' ',list)
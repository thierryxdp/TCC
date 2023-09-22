def retira_pontuacao (frase):
    """retorna uma frase onde todos os caracteres
    de pontuação são substituídos por espaço."""
    frase1 = str.replace(frase,'.',' ')
    frase2 = str.replace(frase1,',',' ')
    frase3= str.replace(frase2,'-',' ')
    frase4 = str.replace(frase3,':',' ')
    frase5 = str.replace(frase4,';',' ')
    frase6 = str.replace(frase5,'!',' ')
    frase7 = str.replace(frase6,'?',' ')
    return frase7

def inverte (fraseinv):
    """ retorna uma outra frase que contenha as palavras na
    ordem inversa e sem letras maiúsculas e sem pontuação."""
    lista = str.split(retira_pontuacao(fraseinv))
    reverteu = list.reverse(lista)
    voltoustr = str(reverteu).strip('[]')
    
    return voltoustr
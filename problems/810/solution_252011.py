def retira_pontuacao(texto):
    '''retorna frase com caracteres de pontuacao substituidos por espaco
    str->str'''
    Frase1=str.replace(texto,'-',' ')
    Frase2=str.replace(Frase1,',',' ')
    Frase3=str.replace(Frase2,':',' ')
    Frase4=str.replace(Frase3,';',' ')
    Frase5=str.replace(Frase4,'.',' ')
    Frase6=str.replace(Frase5,'?',' ')
    Frase7=str.replace(Frase6,'!',' ')
    return Frase7

def
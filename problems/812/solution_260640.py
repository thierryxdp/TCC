def retira_pontuacao(frase):
    """funcao que retorna a frase de entrada onde todos os caracteres de pontuacao tenham sido substituidos por espaco
    str -> str"""
    a=frase
    a=str.replace(a,'-',' ')
    a=str.replace(a,',',' ')
    a=str.replace(a,';',' ')
    a=str.replace(a,'?',' ')
    a=str.replace(a,'!',' ')
    a=str.replace(a,':',' ')
    a=str.replace(a,'.',' ')
    a=str.replace(a,'...',' ')
    return a
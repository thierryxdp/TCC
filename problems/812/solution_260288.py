def retira_pontuacao(frase):
    '''retorna a frase informada com todos os caracteres de pontuação substituidos por um espaço
    str -> str'''
    str.replace(frase,'-',' ')
    str.replace(frase,',',' ')
    str.replace(frase,':',' ')
    str.replace(frase,';',' ')
    str.replace(frase,'.',' ')
    str.replace(frase,'!',' ')
    str.replace(frase,'?',' ')
    return frase
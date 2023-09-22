def retira_pontuacao(frase):
    """ Função que substitui os caracteres de pontuação por espaço
    str -> str """
    frase=str.replace(frase,'-',' ')
    frase=str.replace(frase,',',' ')
    frase=str.replace(frase,':',' ')
    frase=str.replace(frase,';',' ')
    frase=str.replace(frase,'.',' ')
    frase=str.replace(frase,'?',' ')
    frase=str.replace(frase,'!',' ')
    return frase
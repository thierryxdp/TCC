def retira_pontuacao(frase)
    """substitui todos os caracteres de pontuação
    por espaços;
    str->str"""
    frase=str.replace(frase,'-',' ')
    frase=str.replace(frase,',',' ')
    frase=str.replace(frase,':',' ')
    frase=str.replace(frase,';',' ')
    frase=str.replace(frase,'!',' ')
    frase=str.replace(frase,'?',' ')
    frase=str.replace(frase,'.',' ')
    frase=str.replace(frase,'...',' ')
    return frase
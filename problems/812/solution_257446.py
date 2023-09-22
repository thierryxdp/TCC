def retira_pontuacao(frase):
    """Retorna uma nova string sem os caracteres de pontuação da string de entrada;
    str->str"""
    frase=str.replace(frase,'-',' ')
    frase=str.replace(frase,',',' ')
    frase=str.replace(frase,':',' ')
    frase=str.replace(frase,';',' ')
    frase=str.replace(frase,'?',' ')
    frase=str.replace(frase,'.',' ')
    frase=str.replace(frase,'!',' ')
    return frase
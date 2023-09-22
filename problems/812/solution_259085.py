def retira_pontuacao(frase):
    """Função que dada uma frase retorna a mesma com
       os carecteres de pontuação substituídos por
       espaço.
       str->str"""
    frase = str.replace(frase,'.',' ')
    frase = str.replace(frase,',',' ')
    frase = str.replace(frase,';',' ')
    frase = str.replace(frase,'!',' ')
    frase = str.replace(frase,'?',' ')
    frase = str.replace(frase,'-',' ')
    return frase
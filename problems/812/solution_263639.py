def retira_pontuacao(frase):
    """Função que substitui os caracteres de pontuação por espaço.
    str->str"""
    frase1=''
    frase1= str.replace(frase,',',' ')
    frase1= str.replace(frase,'.',' ')
    return frase1
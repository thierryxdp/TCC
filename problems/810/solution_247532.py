def retira_pontuacao(frase):
    """Função que substitui os caracteres de pontuação por espaço.
    str->str"""
    
    return str.replace(str.replace(str.replace(str.replace(str.replace(frase,',',' '),'.',' '),'!',' '),'?',' '),'-',' ')

def inverte(frase):
    """Função que inverte a frase de entrada.
    str->str"""
     return retira_pontuacao[::-1]
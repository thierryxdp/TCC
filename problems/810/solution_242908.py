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
def inverte(frase):
    """ Função que retorna a mesma frase na ordem inversa, sem letras maiúsculas e sem pontuação
    str -> str """
    frase=retira_pontuacao(frase)
    frase=str.lower(frase)
    
    return frase
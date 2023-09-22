def retira_pontuacao(frase):
    """dada a frase, retorna-a com todos os caracteres de pontuação tenham sido substituídos
por espaço.
str->str"""
    frase=str.replace(frase,"!"," ")
    frase=str.replace(frase,"..."," ")
    frase=str.replace(frase,"."," ")
    frase=str.replace(frase,"?"," ")
    frase=str.replace(frase,";"," ")
    frase=str.replace(frase,":"," ")
    frase=str.replace(frase,","," ")
    frase=str.replace(frase,"-"," ")
    return frase

def inverte(frase):
    """ dada a frase, retorna outra com as mesmas palavras na ordem inversa, sem letras
maiúsculas e sem pontuação.
str->str"""
    frase=retira_pontuacao(frase)
    frase=str.lower(frase)
    L1=str.split(frase)
    L2=list.reverse(L1)
    return str.join(L2,' ')
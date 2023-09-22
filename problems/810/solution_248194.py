def retira_pontuacao(frase):
    """ Funçao que, dada uma frase,retorne a frase onde todos os caracteres de pontuação sejam substituidos por espaço"""
    frase=str.replace(frase,"-"," ")
    frase=str.replace(frase,","," ")
    frase=str.replace(frase,":"," ")
    frase=str.replace(frase,";"," ")
    frase=str.replace(frase,"."," ")
    frase=str.replace(frase,"!"," ")
    frase=str.replace(frase,"?"," ")
    frase=str.replace(frase,"..."," ")
    return frase

def inverte(frase):
    """Funçao que, dada uma frase, retorne uma outra frase que contenha
as mesmas palavras dessa frase na ordem inversa, 
sem letras maiusculas e sem pontuaçao"""
    str.lower(frase)
    frase=str.split(frase)
    frase=retira_pontuacao
    inverte=" ".join(retira_pontuacao[::-1])
    return inverte
def retira_pontuacao(frase):
    """dada uma frase, retorne a frase onde todos os caracteres de pontuacao (incluindo travessao, vırgula, dois pontos, ponto e vırgula, alem da pontuacao de encerramento de frase) tenham sido substituıdos por espaço"""
    frase=str.replace(frase,"-"," ")
    frase=str.replace(frase,","," ")
    frase=str.replace(frase,"."," ")
    frase=str.replace(frase,":"," ")
    frase=str.replace(frase,";"," ")
    frase=str.replace(frase,"?"," ")
    frase=str.replace(frase,"!"," ")
    return frase

def inverte(frase):
    """dada uma frase retorne uma outra frase que contenha as mesmas palavras da frase de entrada na ordem inversa, sem letras maiusculas, e sem a pontuaçao"""
    frase=str.lower(frase)
    frase=str.split(frase," ")
    list.reverse(frase)
    frase=str.join("",frase)
    return frase
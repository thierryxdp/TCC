def retira_pontuacao(frase):
    """função que receba uma frase e retorne a frase sem a(as) pontuação(pontuações:'-', ' , ', ':', ';','!',"?","."),ou seja,a pontuação foi substituida por espaço
    str->str"""
    frase=frase.replace('.',' ').replace(',',' ').replace(':',' ').replace('!',' ').replace('-',' ').replace('?',' ').replace(';',' ')
    return frase

def inverte(frase):
    """função que dada uma frase retorne uma outra frase que contenha as mesmas palavras da frase de entrada na ordem inversa, sem letras 
    maiúsculas, e sem a pontuação
    str->str"""
    
    frase=str.lower(frase)
    frase=retira_pontuacao(frase)
    frase=str.split(frase)
    frase=' '.join(frase[::-1])
    return frase
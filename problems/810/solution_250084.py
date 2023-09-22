def retira_pontuacao(x=""):
    '''função que substitui pontuações por espaços na frase'''
    x=x.replace("."," ").replace(";"," ").replace(","," ").replace("-"," ").replace(":"," ").replace("?"," ").replace("!"," ").replace("/"," ")
    return x
def inverte(x=""):
    '''função que retorna outra frase com as mesmas palavras na ordem
    inversa e sem letras maiusculas'''
    x=retira_pontuacao(x).lower()
    x=x.split(" ")
    return str(" ").join(x[::-1])
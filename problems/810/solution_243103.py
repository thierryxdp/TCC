def retira_pontuacao(frase):
    """
    Função que dada uma frase, retorna a frase onde todos os caracteres
    de pontuação tenham sido substituídos por espaço.
    str -> str
    """
    a=str.replace(frase,"..."," ")
    b=str.replace(a,"."," ")
    c=str.replace(b,"!"," ")
    d=str.replace(c,"?"," ")
    e=str.replace(d,"-"," ")
    f=str.replace(e,","," ")
    g=str.replace(f,":"," ")
    h=str.replace(g,";"," ")
    return h

def inverte(frase):
    """
    Função recebe uma frase e retorna outra frase que contenha as mesmas palavras da frase
    de entrada na ordem inversa, sem letras maiúsculas e sem pontuação.
    str -> str
    """
    frase2=retira_pontuacao(frase)
    minuscula=str.split(str.lower(frase2))
    list.reverse(minuscula)
    return str.join(" ",minuscula)
def retira_pontuacao(frase):
    """Retorna a frase de entreda em que todos os caracteres de pontuação são substituidos por espaço. string -> string"""
    F=frase
    F=str.replace(F,"!"," ")
    F=str.replace(F,"."," ")
    F=str.replace(F,"?"," ")
    F=str.replace(F,","," ")
    F=str.replace(F,";"," ")
    F=str.replace(F,"-"," ")
    return F

def inverte(frase):
    """Dada uma frase, chama uma outra frase na ordem inversa, sem letras maiusculas e sem pontuação. string -> string"""
    I=frase
    I=retira_pontuacao(I)
    I=I[::-1]str.join(I)
    return I
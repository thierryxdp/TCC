#str->str
def uppCons(frase):
    "Função que dada uma frase,retorna a frase original com apenas as consoantes em maiusculo."
    frase_nova=''
    posicao=0
    while posicao < len (frase):
        if frase [posicao] in "bcdfgjklmnpqrstvwxz":
            upp=str.upper(frase[posicao])
            frase_nova=frase_nova+upp
            posicao=posicao+1
        elif frase[posicao] not in "bcdfgjklmnpqrstvwxz":
            frase_nova=frase_nova+frase[posicao]
            posicao=posicao+1
    return frase_nova
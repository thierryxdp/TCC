#str->str
def uppCons(frase):
    "Função que dada uma frase,retorna a frase original com apenas as consoantes em maiusculo."
    frase_nova=''
    posicao=0
    while posicao < len(frase):
        if frase [posicao] in 'bcçdfgjklmnpqrstvwxz':
            frase_nova=frase_nova +frase[posicao].upper()
            else:
                frase[posicao] not in 'bçcdfgjklmnpqrstvwxz'
                frase_nova=frase_nova+frase[posicao]
            posicao=posicao+1
    return frase_nova
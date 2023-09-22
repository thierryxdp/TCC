def retira_pontuacao(frase):
    '''Esta e a funcao que dada uma frase, retorna a frase
    onde todos os caracteres de pontuacao tenham sido 
    substituidos por espaco.
    str->str'''
    frase=frase.replace('-',' ')
    frase=frase.replace(',',' ')
    frase=frase.replace(':',' ')
    frase=frase.replace(';',' ')
    frase=frase.replace('.',' ')
    frase=frase.replace('!',' ')
    return frase

def inverte(frase):
    '''Esta e a funcao que dada uma frase, retorna outra
    frase que contem as mesmas palavras da frase de entrada
    na ordem inversa, sem letras maiusculas e sem pontuacao'''
    frase1=retira_pontuacao(frase)
    frase1=frase1.lower()
    frase1=frase1.split()
    f=frase1
    f.reverse()
    return f
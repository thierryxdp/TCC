def retira_pontuacao(frases):
    '''função que substitui todas as pontuações de uma frase por espaços
    str --> str'''
    frase1=frases.replace('!',' ')
    frase2=frase1.replace('?',' ')
    frase3=frase2.replace('...',' ')
    frase4=frase3.replace('.',' ')
    frase5=frase4.replace(':',' ')
    frase6=frase5.replace(';',' ')
    frase7=frase6.replace('-',' ')
    frase8=frase7.replace(',',' ')

    return frase8

def inverte(frase):
    '''função que retorna uma nova frase que contem as mesmas palavras da frase de entrada
    na ordem inversa, sem letras maiusculas e sem pontuação
    str -->str'''
    
    frase1=retira_pontuacao(frase)
    frase2=frase1.lower()
    frase3=frase2.split()
    frase4=frase3[::-1]
    frase5=frase4.join
    return frase5
def retira_pontuacao (frase):
    '''função em que dada uma frase retorne a frase onde todos os caracteres de pontuação tenham sido substituídos por espaços
    str -> str'''
    F1=(str.replace(frase,'!',' '))
    F2=(str.replace(F1,'?',' '))
    F3=(str.replace(F2,'...',' '))
    F4=(str.replace(F3,'.',' '))
    F5=(str.replace(F4,',',' '))
    F6=(str.replace(F5,';',' '))
    F7=(str.replace(F6,':',' '))
    F8=(str.replace(F7,'-',' '))
    return F8

def inverte (texto):
    '''função em que dada uma frase retorne outra frase que contenha as mesmas palavras da frase de entrada na ordem inversa,sem letras maiúsculas e sem pontuação;
    str -> str'''
    F1=(retira_pontuacao(texto))
    F2=str.lower(F1)
    lista=str.split(F2)
    lista.reverse()
    return str.join(' ',lista)
def retira_pontuacao (frase):

    '''função em que dada uma frase retorne a frase onde todos os caracteres de

    pontuação tenham sido substituídos por espaços;

    str -> str'''

    f1=(str.replace(frase,'!',' '))

    f2=(str.replace(f1,'?',' '))

    f3=(str.replace(f2,'...',' '))

    f4=(str.replace(f3,'.',' '))

    f5=(str.replace(f4,',',' '))

    f6=(str.replace(f5,';',' '))

    f7=(str.replace(f6,':',' '))

    f8=(str.replace(f7,'-',' '))

    return f8

def inverte (frase):
    '''função em que dada uma frase retorne outra frase que contenha as mesmas
    palavras da frase de entrada na ordem inversa,sem letras maiúsculas e sem
    pontuação;
    str -> str'''
    f1=(retira_pontuacao(frase))
    f2=str.lower(f1)
    lista=str.split(f2)
    lista.reverse()
    return str.join(' ',lista)
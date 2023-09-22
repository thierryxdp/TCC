def retira_pontuacao(frase):
    '''comentario
    str -> str'''
    f1 = str.replace(frase,'...',' ')
    f2 = str.replace(f1, ',',' ')
    f3 = str.replace(f2,';',' ')
    f4 = str.replace(f3,':',' ')
    f5 = str.replace(f4,'.',' ')
    f6 = str.replace(f5,'?',' ')
    f7 = str.replace(f6,'!',' ')
    f8 = str.replace(f7,'-',' ')
    return f8

def inverte(Frase):
    '''dada uma frase, inverte esta, retira a pontuação e coloca tudo
    em letras minúsculas;
    str -> str'''
    frase = str.lower(Frase)
    sempontuacao = retira_pontuacao(frase)
    palavras = str.split(sempontuacao)
    return str.join(' ',palavras[::-1])
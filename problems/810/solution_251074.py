def retira_pontuacao(frase):
    '''Retira as pontuações da string frase.
   Assinatura: string->string'''
    s1 = frase.replace('.',' ')
    s2 = s1.replace('?',' ')
    s3=s2.replace('!',' ')
    s4 =s3.replace('-',' ')
    s5=s4.replace(',',' ')
    s6 = s5.replace(':',' ')
    s7=s6.replace(';',' ')
    return s7
def inverte(frase):
    '''Inverte uma string frase.
    Assinatura: string->string'''
    f1 = retira_pontuacao(frase).lower()
    f2 = f1.split('')
    return f2
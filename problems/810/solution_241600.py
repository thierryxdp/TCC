def retira_pontuacao(frase):
    '''Função que retira as pontuações('-',',',':',';','.')
    de uma dada frase.
    str ->str'''
    f2=frase.replace('-',' ')
    f2=f2.replace(',',' ')
    f2=f2.replace(':',' ')
    f2=f2.replace(';',' ')
    f2=f2.replace('.',' ')
    f2=f2.replace('!',' ')
    f2=f2.replace('?',' ')
    return f2.strip(' ')

def inverte(frase):
    '''Função que inverte a frase dada.
    str ->str'''
    return frase.reverse()
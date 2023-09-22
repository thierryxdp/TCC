def retira_pontuacao(f):
    '''Retira todos os caracteres de pontuação de uma frase f
    str -> str'''
    k='-,:;.!?'

    list.replace(f,'-','')
    list.replace(f,',','')
    list.replace(f,':','')
    list.replace(f,';','')
    list.replace(f,'.','')
    list.replace(f,'!','')
    list.replace(f,'?','')
    return f
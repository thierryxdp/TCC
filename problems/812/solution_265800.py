def retira_pontuacao(f):
    '''Retira todos os caracteres de pontuação de uma frase f
    str -> str'''
    k='-,:;.!?'
    str.replace(f,'-','')
    str.replace(f,',','')
    str.replace(f,':','')
    str.replace(f,';','')
    str.replace(f,'.','')
    str.replace(f,'!','')
    str.replace(f,'?','')
    return f
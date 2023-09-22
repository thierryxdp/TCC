def retira_pontuacao(f):
    '''Retira todos os caracteres de pontuação de uma frase f
    str -> str'''
    k='-,:;.!?'
    if x in k:
        str.replace(f,x,'')

    str.replace(f,'-','')
    str.replace(f,',','')
    str.replace(f,':','')
    str.replace(f,';','')
    str.replace(f,'.','')
    str.replace(f,'!','')
    str.replace(f,'?','')
    return f
def retira_pontuacao(f):
    '''Retira todos os caracteres de pontuação de uma frase f
    str -> str'''
    k='-,:;.!?'
    for x in range(len(k)):
        f=f.replace(f[x],'')
    return f
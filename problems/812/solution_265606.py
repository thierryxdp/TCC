def retira_pontuacao(frase):
    a='-,:;....?!'
    for i in range(0,len(frase)):
        a=a.replace(i,' ')
    return frase
def retira_pontuacao(frase):
    str.partition(frase,'.')
    str.partition(frase,'...')
    str.partition(frase,'!')
    str.partition(frase,'?')
    str.partition(frase,',')
    str.partition(frase,'-')
    str.partition(frase,';')
    str.partition(frase,':')
    return frase
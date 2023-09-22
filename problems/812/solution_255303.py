def retira_pontuação (x):
    '''Função que dada uma frase, retorna esta frase com espaços
    no lugar de qualquer tipo de pontuação encontrados (travessão,
    virgula, dois pontos, ponto e virgula e pontuação de encerramento)
    string->string'''
    str.replace (x,'-',' ')
    str.replace (x,',',' ')
    str.replace (x,':',' ')
    str.replace (x,';',' ')
    str.replace (x,'.',' ')
    str.replace (x,'?',' ')
    str.replace (x,'!',' ')
    str.replace (x,'...',' ')
    return x
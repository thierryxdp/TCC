def retira_pontuacao(pontuacao):
    ''' funcao que recebe uma frase e transforma seus caracteres de pontuacao em espaco '''
    caracteres= ['/', '?', ',', '.', '...', ';', ':']
    split_pontuacao = pontuacao.list(caracteres[])
    return split_pontuacao
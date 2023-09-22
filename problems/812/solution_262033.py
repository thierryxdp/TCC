def retira_pontuacao(pontuacao):
    ''' funcao que recebe uma frase e transforma seus caracteres de pontuacao em espaco '''
    caracteres= ['/', '?', ',', '.', '...', ';', ':']
    replace_pontuacao = pontuacao.list(caracteres[0])
    return replace_pontuacao
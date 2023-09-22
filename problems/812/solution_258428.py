def retira_pontuacao(frase):
    '''retira as pontuações da frase substituindo por espaços
    str -> str'''
    pontuacoes = ['.','-',',',':',';','!','?']
    return str.replace(frase,['.','-',',',':',';','!','?'],' ')
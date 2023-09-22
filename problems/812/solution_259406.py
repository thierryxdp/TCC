def verifica_pontuacao(c):
    '''Verifica se o caractere é algum tipo de pontuação, caso 
    positivo o troca por espaço (' ')'''
    pontuacao = ['.', ',', '-', ';', '?', '!', ':']
    return c if c in pontuacao else '' ' '
def retira_pontuacao(frase):
    return ''.join(list(map(verifica_pontuacao, list(frase))))
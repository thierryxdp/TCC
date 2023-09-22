def verifica_pontuacao(c):
    '''Verifica se o caractere é algum tipo de pontuação, caso 
    positivo o troca por espaço (' ')'''
    pontuacao = ['.', ',', '-', ';', '?', '!', ':']
    return c if c not in pontuacao else ' '
def retira_pontuacao(frase):
    '''Retorna a frase recebida com todos os caracteres de pontuação
    substituídos por espaço'''
    return ''.join(list(map(verifica_pontuacao, list(frase))))
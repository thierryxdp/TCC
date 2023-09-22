# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''
        Função que insere # no início, meio e fim de um string.
        Valor de entrada: string
        Valor de retorno: string
        '''
        return '#' + s[0:len(s)//2] + '#' + s[len(s)//2:] + '#'
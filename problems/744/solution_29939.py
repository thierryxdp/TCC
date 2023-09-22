# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Retorna palavra com # no início, no meio e no fim.
    Inserir palavra entre aspas.
    str-> str '''
    
    caracter_meio = len(s)//2
    parte1 = s[0:caracter_meio]
    parte2 = s[caracter_meio:len(s)]
    return '#' + parte1 + '#' + parte2 + '#'
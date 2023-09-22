# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''funcao que retorna uma string com # no comeco,
    meio e fim.
    entrada: string
    saida: string
    '''
    string= str(s)
    primeiraParte= s[0:(len(s)//2)]
    segundaParte= s[(len(s)//2):]
    return '#'+primeiraParte+'#'+segundaParte+'#'
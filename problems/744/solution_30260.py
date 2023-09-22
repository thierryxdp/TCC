# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Função que retorna a adição de '#' (hastags)
    ao parâmetro de entrada da função, uma string, de tamanho
    qualquer, digitada pelo usuário. String-->String'''
    return '#'+s[:len(s)//2:]+'#'+s[len(s)//2::]+'#'
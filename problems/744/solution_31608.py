# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''
    retorna a string escolhida mas com # no comeco, no e no final
    param s: str
    return: str
    '''
    s =  s[::] + '#'+ s[::] 
    return '#' + s + '#'
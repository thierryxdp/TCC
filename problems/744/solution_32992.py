# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''
    Função que recebe uma string e a retorna fracionada
    com três hashtags, cada uma no início, meio e fim
    s = string a ser recebida
    str -> str
    '''
    caracteres = len(s)
    centro_str = caracteres//2
    metade_1 = s[0:centro_str]
    metade_2 = s[centro_str:caracteres]
    return '#' + metade_1 + '#' + metade_2 + '#'
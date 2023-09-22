# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    'Retorna a string s digitada com o símbolo # no início,meio e fim dela.str ->str'
    i = len(s) 
    a = int(i/2)
    s1,s2 = s[:a],s[a:]
    return '#' + s1 +'#'+ s2 + '#'